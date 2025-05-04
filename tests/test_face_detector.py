import numpy as np
import cv2
from src.face_detector import get_face_cascade, detect_faces

def test_detect_faces_with_blank_image():
    cascade = get_face_cascade()
    blank = np.zeros((512, 512, 3), dtype=np.uint8)
    faces = detect_faces(blank, cascade)
    assert isinstance(faces, (list, tuple))