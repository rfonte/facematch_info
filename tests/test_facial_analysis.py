# tests/test_facial_analysis.py
import pytest
import numpy as np
from src.facial_analysis import analyze_face

def test_analyze_face_invalid():
    with pytest.raises(Exception):
        dummy_img = np.zeros((10, 10, 3), dtype=np.uint8)
        analyze_face(dummy_img)
