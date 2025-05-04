📸 FaceMatch Info – Análise Facial com DeepFace e OpenCV
Este projeto realiza detecção de rostos em tempo real via webcam, usando OpenCV e analisa características como idade, gênero e emoção dominante com DeepFace. O resultado é exibido na tela com um retângulo ao redor do rosto e informações sobre a pessoa detectada.

🧠 Funcionalidades
📷 Captura de vídeo em tempo real via webcam

😎 Detecção de rostos com HaarCascade (OpenCV)

🤖 Análise facial com DeepFace (idade, gênero, emoção)

🖼️ Sobreposição de dados diretamente no frame da câmera

📝 Log completo das análises salvas em arquivo

✅ Estrutura modular com testes automatizados

🗂️ Estrutura de Diretórios

facematch_info/
├── main.py                     # Ponto de entrada da aplicação
├── src/
│   ├── logger_config.py        # Configuração do sistema de log
│   ├── face_detector.py        # Módulo de detecção de rostos
│   └── facial_analysis.py      # Módulo de análise com DeepFace
├── tests/
│   └── test_face_modules.py    # Testes unitários básicos
├── log_analise_facial.log      # Arquivo de log da sessão atual
└── requirements.txt            # Lista de dependências

▶️ Como Executar
0. Crie o ambiente virtual:
    py -3.10 -m venv venv_deepface
    venv_deepface\Scripts\activate

1. Clone o repositório:
    git clone https://github.com/seu-usuario/facematch_info.git
    cd facematch_info
2. Crie o ambiente virtual e ative:
    py -3.10 -m venv venv_deepface
    venv\Scripts\activate  # No Windows
3. Instale as dependências:
    pip install -r requirements.txt
4. Execute o sistema:
    python main.py

🧪 Como Executar os Testes
    pytest tests/

🛠️ Tecnologias Utilizadas
OpenCV - https://opencv.org/
DeepFace - https://github.com/serengil/deepface
Python 3.8+ - https://www.python.org/
pytest - https://docs.pytest.org/en/7.2.x/

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.