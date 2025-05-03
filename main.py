import cv2
from deepface import DeepFace

# Inicializa a webcam (0 = câmera padrão)
cap = cv2.VideoCapture(0)

print("Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao acessar a webcam.")
        break

    # Reduz o tamanho da imagem para melhorar o desempenho
    resized_frame = cv2.resize(frame, (640, 480))

    try:
        # Analisa a face na imagem capturada
        results = DeepFace.analyze(resized_frame,
                                   actions=['age', 'gender', 'emotion'],
                                   enforce_detection=False)

        # Extrai os dados do resultado
        age = results[0]['age']
        gender = results[0]['gender']
        emotion = results[0]['dominant_emotion']

        # Escreve as informações na tela da webcam
        text = f"Idade: {age} | Gênero: {gender} | Emoção: {emotion}"
        cv2.putText(resized_frame, text, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    except Exception as e:
        print("Erro na análise facial:", e)

    # Exibe o vídeo com overlay
    cv2.imshow("Análise Facial com IA - Pressione 'q' para sair", resized_frame)

    # Sai ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha a janela
cap.release()
cv2.destroyAllWindows()