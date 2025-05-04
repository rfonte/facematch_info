# main.py
import cv2
from src.logger_config import setup_logger
from src.face_detector import get_face_cascade, detect_faces
from src.facial_analysis import analyze_face

logger = setup_logger()

face_cascade = get_face_cascade()
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    logger.error("Não foi possível abrir a câmera.")
    print("Erro: Não foi possível abrir a câmera.")
    exit()

print("Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        logger.warning("Falha ao capturar frame da webcam.")
        continue

    faces = detect_faces(frame, face_cascade)

    if len(faces) == 0:
        msg = "Nenhum rosto detectado com HaarCascade."
        print(msg)
        logger.info(msg)
    else:
        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]
            try:
                result = analyze_face(face_img)
                data = result[0] if isinstance(result, list) else result
                age = data.get("age", "?")
                gender = data.get("gender", "?")
                emotion = data.get("dominant_emotion", "?")

                label = f"{gender}, {age} anos, {emotion}"
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                print(f"Análise: {data}")
                logger.info(f"Análise: {data}")
            except Exception as e:
                msg = f"Erro na análise facial: {str(e)}"
                print(msg)
                logger.error(msg)

    cv2.imshow("Webcam - Detecção Facial", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
logger.info("Encerrado com sucesso.")