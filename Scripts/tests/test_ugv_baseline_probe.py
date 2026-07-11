import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).parents[1] / "mworks" / "ugv_baseline_probe.py"
SPEC = importlib.util.spec_from_file_location("ugv_baseline_probe", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class TrackCompletionClassificationTests(unittest.TestCase):
    def test_official_origin_assertion_is_finish(self):
        self.assertEqual(
            MODULE.classify_track_completion(17.4, 0.019, False),
            "finish_reached_official_origin_assertion",
        )

    def test_horizon_without_origin_return_is_not_finish(self):
        self.assertEqual(
            MODULE.classify_track_completion(120.0, 12.0, True),
            "simulation_horizon_reached_finish_not_observed",
        )

    def test_horizon_return_near_origin_is_not_finish(self):
        self.assertEqual(
            MODULE.classify_track_completion(17.4, 0.019, True),
            "simulation_horizon_reached_finish_not_observed",
        )

    def test_early_stop_away_from_origin_is_not_finish(self):
        self.assertEqual(
            MODULE.classify_track_completion(50.2, 2.0, False),
            "early_stop_finish_not_observed",
        )


class ManifestNotesTests(unittest.TestCase):
    def test_official_finish_assertion_is_described_as_finish(self):
        notes = MODULE.manifest_notes(
            "finish-run",
            {
                "runtime_status": "simulate_failed",
                "completion": "finish_reached_official_origin_assertion",
            },
        )

        self.assertTrue(any("Official track finish was observed" in note for note in notes))
        self.assertFalse(any("did not prove" in note for note in notes))

    def test_horizon_run_does_not_claim_finish(self):
        notes = MODULE.manifest_notes(
            "horizon-run",
            {
                "runtime_status": "simulate_returned_true",
                "completion": "simulation_horizon_reached_finish_not_observed",
            },
        )

        self.assertTrue(any("finish was not observed" in note for note in notes))


if __name__ == "__main__":
    unittest.main()
