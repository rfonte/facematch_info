# src/cli.py
import cv2

from . import logger_config, face_detector, facial_analysis


def main(camera_index: int = 0, show_gui: bool = True, log_filename: str | None = None):
    """Run the facial analysis loop.

    Parameters:
    - camera_index: index of the camera for `cv2.VideoCapture`.
    - show_gui: whether to call `cv2.imshow` (useful for headless testing).
    - log_filename: optional path to pass to `setup_logger`.
    """
    logger = logger_config.setup_logger(log_filename) if log_filename else logger_config.setup_logger()

    face_cascade = face_detector.get_face_cascade()
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        logger.error("Não foi possível abrir a câmera.")
        print("Erro: Não foi possível abrir a câmera.")
        raise SystemExit(1)

    print("Pressione 'q' para sair.")

    while True:
        ret, frame = cap.read()
        if not ret:
            logger.warning("Falha ao capturar frame da webcam.")
            continue

        faces = face_detector.detect_faces(frame, face_cascade)

        if len(faces) == 0:
            msg = "Nenhum rosto detectado com HaarCascade."
            print(msg)
            logger.info(msg)
        else:
            for (x, y, w, h) in faces:
                face_img = frame[y:y+h, x:x+w]
                try:
                    result = facial_analysis.analyze_face(face_img)
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

        if show_gui:
            cv2.imshow("Webcam - Detecção Facial", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    logger.info("Encerrado com sucesso.")


if __name__ == "__main__":
    main()