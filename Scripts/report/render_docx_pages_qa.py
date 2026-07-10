#!/usr/bin/env python3
"""Render a DOCX report to PDF/PNG pages and write page-level QA evidence.

This is a report-quality helper. It does not run MWORKS, change model source,
create a submission zip, or send a competition email.
"""
from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageStat


PDF_FORMAT = 17
WORD_PAGE_COUNT_STAT = 2


def export_with_word(docx: Path, pdf: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "method": "word_com",
        "docx": str(docx),
        "pdf": str(pdf),
        "status": "unknown",
    }
    word = None
    try:
        import win32com.client

        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False
        word.DisplayAlerts = 0
        doc = word.Documents.Open(str(docx), ReadOnly=True, AddToRecentFiles=False)
        doc.ExportAsFixedFormat(
            OutputFileName=str(pdf),
            ExportFormat=PDF_FORMAT,
            OpenAfterExport=False,
            OptimizeFor=0,
            Range=0,
            Item=0,
            IncludeDocProps=True,
            KeepIRM=True,
            CreateBookmarks=1,
            DocStructureTags=True,
            BitmapMissingFonts=True,
            UseISO19005_1=False,
        )
        result["page_count_word"] = int(doc.ComputeStatistics(WORD_PAGE_COUNT_STAT))
        doc.Close(False)
        result["status"] = "ok"
    except Exception as exc:  # pragma: no cover - depends on local Office install.
        result["status"] = "failed"
        result["error"] = repr(exc)
    finally:
        try:
            if word is not None:
                word.Quit()
        except Exception:
            pass
    result["pdf_exists"] = pdf.exists()
    result["pdf_size_bytes"] = pdf.stat().st_size if pdf.exists() else 0
    return result


def export_with_soffice(docx: Path, pdf: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "method": "soffice",
        "docx": str(docx),
        "pdf": str(pdf),
        "status": "unknown",
    }
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        result["status"] = "unavailable"
        result["error"] = "soffice/libreoffice not found"
        return result

    cp = subprocess.run(
        [
            soffice,
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            str(pdf.parent),
            str(docx),
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    generated = pdf.parent / f"{docx.stem}.pdf"
    if generated.exists() and generated != pdf:
        generated.replace(pdf)
    result.update(
        {
            "returncode": cp.returncode,
            "stdout": cp.stdout,
            "stderr": cp.stderr,
            "pdf_exists": pdf.exists(),
            "pdf_size_bytes": pdf.stat().st_size if pdf.exists() else 0,
            "status": "ok" if cp.returncode == 0 and pdf.exists() else "failed",
        }
    )
    return result


def find_pdftoppm() -> str | None:
    bundled = (
        Path.home()
        / ".cache"
        / "codex-runtimes"
        / "codex-primary-runtime"
        / "dependencies"
        / "native"
        / "poppler"
        / "Library"
        / "bin"
        / "pdftoppm.exe"
    )
    if bundled.exists():
        return str(bundled)
    return shutil.which("pdftoppm")


def render_pdf_pages(pdf: Path, out_dir: Path, dpi: int) -> dict[str, Any]:
    pdftoppm = find_pdftoppm()
    result: dict[str, Any] = {"method": "pdftoppm", "pdftoppm": pdftoppm}
    if not pdftoppm:
        result["status"] = "unavailable"
        result["error"] = "pdftoppm not found"
        return result
    prefix = out_dir / "page"
    cp = subprocess.run(
        [pdftoppm, "-png", "-r", str(dpi), str(pdf), str(prefix)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    pages = sorted(out_dir.glob("page-*.png"))
    result.update(
        {
            "status": "ok" if cp.returncode == 0 and pages else "failed",
            "returncode": cp.returncode,
            "stdout": cp.stdout,
            "stderr": cp.stderr,
            "page_files": [p.name for p in pages],
        }
    )
    return result


def build_contact_sheet(pages: list[Path], contact_sheet: Path) -> list[dict[str, Any]]:
    page_infos = []
    thumbs = []
    for page in pages:
        im = Image.open(page).convert("RGB")
        width, height = im.size
        small = im.resize((max(1, width // 8), max(1, height // 8)))
        pixels = list(small.getdata())
        nonwhite = sum(1 for r, g, b in pixels if min(r, g, b) < 245)
        nonwhite_ratio = nonwhite / len(pixels)
        stat = ImageStat.Stat(small)
        page_infos.append(
            {
                "file": page.name,
                "width": width,
                "height": height,
                "size_bytes": page.stat().st_size,
                "nonwhite_ratio": round(nonwhite_ratio, 5),
                "channel_mean": [round(value, 2) for value in stat.mean],
            }
        )
        thumb_width = 260
        thumb_height = int(height * thumb_width / width)
        thumbs.append((page.name, im.resize((thumb_width, thumb_height))))

    if not thumbs:
        return page_infos

    cols = 2
    label_height = 24
    pad = 18
    cell_width = max(thumb.size[0] for _, thumb in thumbs) + pad * 2
    cell_height = max(thumb.size[1] for _, thumb in thumbs) + label_height + pad * 2
    rows = math.ceil(len(thumbs) / cols)
    sheet = Image.new("RGB", (cols * cell_width, rows * cell_height), "white")
    draw = ImageDraw.Draw(sheet)
    for index, (name, thumb) in enumerate(thumbs):
        x = (index % cols) * cell_width + pad
        y = (index // cols) * cell_height + pad
        draw.text((x, y), name, fill=(0, 0, 0))
        sheet.paste(thumb, (x, y + label_height))
    sheet.save(contact_sheet)
    return page_infos


def build_qa(docx: Path, out_dir: Path, dpi: int, min_pages: int) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf = out_dir / f"{docx.stem}_word_export.pdf"
    export = export_with_word(docx, pdf)
    if export["status"] != "ok":
        pdf = out_dir / f"{docx.stem}_soffice_export.pdf"
        export = export_with_soffice(docx, pdf)
    render = render_pdf_pages(pdf, out_dir, dpi) if export["status"] == "ok" else {
        "status": "skipped",
        "reason": "pdf_export_failed",
    }
    pages = sorted(out_dir.glob("page-*.png"))
    contact_sheet = out_dir / "contact_sheet.png"
    page_infos = build_contact_sheet(pages, contact_sheet)
    suspected_blank_pages = [
        row["file"] for row in page_infos if row["nonwhite_ratio"] < 0.01
    ]
    status = "passed"
    if export["status"] != "ok" or render["status"] != "ok":
        status = "failed"
    elif len(pages) < min_pages or suspected_blank_pages:
        status = "review_required"

    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "docx": str(docx),
        "output_dir": str(out_dir),
        "pdf": str(pdf),
        "export": export,
        "render": render,
        "page_count": len(pages),
        "min_pages": min_pages,
        "contact_sheet": str(contact_sheet),
        "blank_page_threshold_nonwhite_ratio": 0.01,
        "pages": page_infos,
        "suspected_blank_pages": suspected_blank_pages,
        "status": status,
        "non_claims": [
            "Does not approve final competition submission.",
            "Does not run MWORKS.",
            "Does not create a final zip.",
        ],
    }


def write_note(qa: dict[str, Any], path: Path) -> None:
    lines = [
        "# Report Page Render QA",
        "",
        f"status: {qa['status']}",
        f"timestamp: {qa['timestamp']}",
        "",
        "## Inputs",
        "",
        f"- DOCX: `{qa['docx']}`",
        f"- PDF: `{qa['pdf']}`",
        f"- contact_sheet: `{qa['contact_sheet']}`",
        "",
        "## Checks",
        "",
        f"- PDF export method: `{qa['export']['method']}`",
        f"- PDF export status: `{qa['export']['status']}`",
        f"- page_count: `{qa['page_count']}`",
        f"- min_pages: `{qa['min_pages']}`",
        f"- suspected_blank_pages: `{qa['suspected_blank_pages']}`",
        "",
        "## Page Files",
        "",
    ]
    for row in qa["pages"]:
        lines.append(
            f"- `{row['file']}`: size={row['width']}x{row['height']}, "
            f"nonwhite_ratio={row['nonwhite_ratio']}"
        )
    lines.extend(["", "## Non-Claims", ""])
    for item in qa["non_claims"]:
        lines.append(f"- {item}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docx", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--dpi", type=int, default=130)
    parser.add_argument("--min-pages", type=int, default=1)
    parser.add_argument("--json-out")
    parser.add_argument("--md-out")
    parser.add_argument("--fail-on-not-passed", action="store_true")
    args = parser.parse_args()

    qa = build_qa(Path(args.docx).resolve(), Path(args.out_dir).resolve(), args.dpi, args.min_pages)
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.md_out:
        write_note(qa, Path(args.md_out))
    print(json.dumps({"status": qa["status"], "page_count": qa["page_count"]}, ensure_ascii=False))
    if args.fail_on_not_passed and qa["status"] != "passed":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
