[![Coverage](https://codecov.io/gh/rfonte/facematch_info/branch/main/graph/badge.svg)](https://codecov.io/gh/rfonte/facematch_info)

**FaceMatch Info — Análise Facial (DeepFace + OpenCV)**

Projeto para detecção e análise facial em tempo real via webcam. Usa OpenCV para captura e detecção de faces e DeepFace para análise de atributos como idade, gênero e emoção dominante. Resultados são sobrepostos no vídeo e gravados em log para auditoria.

**Principais Funcionalidades**
- **Captura:** Vídeo em tempo real via webcam.
- **Detecção:** Faces detectadas com HaarCascade / OpenCV.
- **Análise:** Predição de idade, gênero e emoção com DeepFace.
- **Overlay:** Exibição de retângulo e informações sobre o frame.
- **Logging:** Registros das análises salvos em arquivo.
- **Testes:** Testes básicos com `pytest`.

**Estrutura do Projeto**
- [main.py](main.py) — Ponto de entrada da aplicação.
- [src/](src/) — Código fonte do projeto:
  - [src/logger_config.py](src/logger_config.py) — Configuração do logging.
  - [src/face_detector.py](src/face_detector.py) — Detecção de faces (OpenCV).
  - [src/facial_analysis.py](src/facial_analysis.py) — Integração com DeepFace.
- [models/](models/) — Modelos e pesos (não versionados aqui).
- [tests/](tests/) — Testes unitários (`pytest`).
- [requirements.txt](requirements.txt) — Dependências do projeto.
- [LICENSE](LICENSE) — Licença MIT.

**Pré-requisitos**
- Python 3.10 (recomendado).
- GPU compatível (opcional) para acelerar DeepFace/TensorFlow.

No Windows, comandos de exemplo:

```powershell
py -3.10 -m venv venv_deepface
venv_deepface\Scripts\Activate.ps1  # PowerShell
pip install -r requirements.txt
```

**Como Executar**
1. Ative o ambiente virtual (veja acima).
2. Ajuste a câmera padrão se necessário (configuração no `main.py`).
3. Execute:

```powershell
python main.py
```

Ao iniciar, uma janela com o feed da webcam será aberta. Faces detectadas terão um retângulo e texto com as predições.

**Testes**
Executar a suíte de testes com `pytest`:

```powershell
pytest tests/
```

**Geração de Documentação**
Se desejar gerar documentação HTML (requer `pdoc`):

```powershell
pip install pdoc
pdoc --output-dir docs src
```

**Configuração e Logs**
- Arquivo de configuração de logs: [src/logger_config.py](src/logger_config.py).
- O log de execução padrão é gravado em `log_analise_facial.log` no diretório do projeto.

Logs e rotação
- O logger usa rotação por tempo por padrão (`TimedRotatingFileHandler`, rotações a cada `midnight`),
  mantendo por padrão `backup_count=7` arquivos antigos. É possível configurar para rotação por tamanho.

Exemplos de uso do `setup_logger` (em `src/logger_config.py`):

```python
from src.logger_config import setup_logger

# Time-based rotation (padrão): rotaciona diariamente e mantém 7 arquivos
logger = setup_logger("logs/app.log", rotation="time", when="midnight", interval=1, backup_count=7)

# Size-based rotation: rotaciona ao atingir 5MB e mantém 5 backups
logger = setup_logger("logs/app.log", rotation="size", max_bytes=5*1024*1024, backup_count=5)
```

**Boas Práticas / Observações**
- Modelos DeepFace podem baixar pesos na primeira execução — aguarde a inicialização.
- Em máquinas sem GPU, a inicialização pode demorar bastante; considere usar uma máquina com GPU ou um runtime em nuvem para testes pesados.
- Para melhorar performance em tempo real, reduza a resolução do frame antes da análise.

**Possíveis Problemas e Soluções**
- Erro de importação do `cv2`: verifique se `opencv-python` está instalado no ambiente ativo.
- Erros de versão TensorFlow/DeepFace: use as versões listadas em `requirements.txt` do projeto ou crie um ambiente isolado com as versões compatíveis.

**Contribuindo**
Pull requests são bem-vindos. Para contribuir:

1. Fork do repositório.
2. Crie uma branch com a feature/bugfix.
3. Abra um PR descrevendo as mudanças e testes realizados.

**Licença**
Projeto licenciado sob MIT — veja [LICENSE](LICENSE).

**Contato / Referências**
- DeepFace: https://github.com/serengil/deepface
- OpenCV: https://opencv.org/

--
Atualizado para fornecer instruções claras de uso, testes, geração de docs, deploy local e contribuições.