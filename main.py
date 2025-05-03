import cv2
import logging
from deepface import DeepFace

# ========== CONFIGURAÇÃO DO LOG ========== #
log_filename = "log_analise_facial.log"
with open(log_filename, "w"):  # Limpa o arquivo a cada execução
    pass

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ========== DETECTOR DE ROSTO DO OPENCV PARA DEBUG ========== #
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# ========== INICIALIZA A CÂMERA ========== #
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    logging.error("Não foi possível abrir a câmera.")
    print("Erro: Não foi possível abrir a câmera.")
    exit()

print("Pressione 'q' para sair.")

# ========== LOOP PRINCIPAL ========== #
while True:
    ret, frame = cap.read()
    if not ret:
        logging.warning("Falha ao capturar frame da webcam.")
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) == 0:
        msg = "Nenhum rosto detectado com HaarCascade."
        print(msg)
        logging.info(msg)
    else:
        try:
            result = DeepFace.analyze(
                frame,
                actions=['gender', 'age', 'emotion'],
                enforce_detection=True
            )
            logging.info(f"Resultado: {result}")
            print(f"Análise: {result[0] if isinstance(result, list) else result}")
        except Exception as e:
            msg = f"DeepFace não conseguiu analisar: {str(e)}"
            print(msg)
            logging.error(msg)

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ========== FINALIZA ========== #
cap.release()
cv2.destroyAllWindows()
logging.info("Encerrado com sucesso.")