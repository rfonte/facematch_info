import numpy as np
import pytest
from src.facial_analysis import analyze_face

def test_analyze_face_invalid():
    blank_image = np.zeros((10, 10, 3), dtype=np.uint8)
    with pytest.raises(Exception):
        analyze_face(blank_image, enforce_detection=True)