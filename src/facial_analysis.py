# src/facial_analysis.py
from deepface import DeepFace

def analyze_face(face_img):
    return DeepFace.analyze(
        face_img,
        actions=['gender', 'age', 'emotion'],
        enforce_detection=False
    )