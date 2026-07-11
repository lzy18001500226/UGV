import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).parents[1] / "analysis" / "analyze_track_geometry.py"
SPEC = importlib.util.spec_from_file_location("analyze_track_geometry", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class AnalyzeTrackGeometryTests(unittest.TestCase):
    def test_extract_and_analyze_small_model(self):
        source = "inner Road.TabularRoadObstacle road(roadMap = {{0,0,2}, {3,0,2}, {3,4,2}},\n surface());"
        model = Path(self._testMethodName + ".mo")
        try:
            model.write_text(source, encoding="utf-8")
            rows = MODULE.extract_road_map(model)
            result = MODULE.analyze_road_map(rows)
        finally:
            model.unlink(missing_ok=True)
        self.assertEqual(rows, [[0, 0, 2], [3, 0, 2], [3, 4, 2]])
        self.assertAlmostEqual(result["closed_loop_length_m"], 12.0)
        self.assertAlmostEqual(result["ideal_time_at_map_speed_s"], 6.0)

    def test_rejects_missing_map(self):
        model = Path(self._testMethodName + ".mo")
        try:
            model.write_text("model Empty end Empty;", encoding="utf-8")
            with self.assertRaises(ValueError):
                MODULE.extract_road_map(model)
        finally:
            model.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
