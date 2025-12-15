import numpy as np
import pytest
from src import facial_analysis


def test_analyze_face_success(monkeypatch):
    dummy = np.zeros((100, 100, 3), dtype=np.uint8)
    expected = {"age": 30, "gender": "Man", "emotion": {"dominant": "neutral"}}

    class DummyDeepFace:
        @staticmethod
        def analyze(img, actions, enforce_detection):
            assert actions == ["gender", "age", "emotion"]
            return expected

    monkeypatch.setattr(facial_analysis, "DeepFace", DummyDeepFace)
    result = facial_analysis.analyze_face(dummy)
    assert result == expected


def test_analyze_face_propagates_exception(monkeypatch):
    dummy = np.zeros((10, 10, 3), dtype=np.uint8)

    class DummyDeepFace:
        @staticmethod
        def analyze(img, actions, enforce_detection):
            raise ValueError("failed")

    monkeypatch.setattr(facial_analysis, "DeepFace", DummyDeepFace)
    with pytest.raises(ValueError):
        facial_analysis.analyze_face(dummy)
