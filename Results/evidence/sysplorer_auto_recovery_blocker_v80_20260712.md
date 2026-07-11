# Sysplorer automatic-recovery blocker

Status: human decision required before deleting or restoring backup data.

## Observation

An unchanged committed-v80 Track2 1 s control probe remained inside
`StartSysplorer`. The visible Sysplorer window was responsive and titled
`Sysplorer [演示版]`, but a modal `自动恢复` window blocked startup.

The modal reported an abnormal prior exit and listed a selected UGV model
backup created at approximately `2026-07-12 00:46:18`. Attempting to close the
modal produced a second confirmation:

```text
其他所有备份将被丢弃，是否继续？
```

The destructive confirmation was not accepted. The backup was not restored or
discarded. The waiting probe Python process was stopped; the responsive
Sysplorer window and recovery UI were left available for review.

## Why this blocks autonomous recovery

- Choosing restore can overwrite current project model files, potentially
  including official no-edit areas or the committed v80 baseline.
- Choosing continue/discard deletes automatic-recovery backup data and requires
  explicit action-time confirmation.
- The control probe proves the block is independent of v131 source because the
  source hashes matched committed v80 before launch.

## Required decision

Approve one of:

1. Discard the listed automatic-recovery backup and continue with committed
   Git source; recommended because the committed v80 hashes are already
   verified.
2. Preserve and manually inspect/restore the backup before continuing; this
   requires a separate diff audit before any runtime claim.

## Recovery gate

After the modal is resolved, rerun the unchanged v80 1 s probe first. Recovery
is proven only when evidence reaches `open_model_file`, `check_model`, and
`simulate_returned_true`. Only then may v131 be reapplied and tested.

## Non-claims

- No v80 runtime recovery yet.
- No v131 runtime result.
- No official finish or score improvement.
