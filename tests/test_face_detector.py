# tests/test_face_detector.py
import cv2
from src.face_detector import get_face_cascade, detect_faces

def test_get_face_cascade():
    cascade = get_face_cascade()
    assert cascade is not None

def test_detect_faces_with_blank_image():
    cascade = get_face_cascade()
    blank = cv2.imread(cv2.samples.findFile("lena.jpg"))
    faces = detect_faces(blank, cascade)
    assert isinstance(faces, tuple) or isinstance(faces, list)
