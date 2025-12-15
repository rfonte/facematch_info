import numpy as np
import pytest
import cv2
from src.face_detector import get_face_cascade, detect_faces


def test_get_face_cascade_loads():
    cascade = get_face_cascade()
    assert cascade is not None
    # CascadeClassifier.empty() is False when cascade loaded correctly
    assert not cascade.empty()


def test_detect_faces_with_wrong_shape():
    cascade = get_face_cascade()
    gray = np.zeros((512, 512), dtype=np.uint8)
    with pytest.raises(Exception):
        detect_faces(gray, cascade)


def test_detect_faces_invalid_input():
    cascade = get_face_cascade()
    with pytest.raises(Exception):
        detect_faces(None, cascade)
