# Projeto de Vigilância com Reconhecimento Facial - Roadmap

## Objetivo Geral
Desenvolver um sistema de vigilância doméstica com reconhecimento facial que registre **quem**, **quando** e **onde** uma pessoa foi detectada, armazenando essas informações em um backend e exibindo os dados por meio de uma interface web.

---

## Fase 1: MVP Local com Webcam + Reconhecimento Facial

### Requisitos de Negócio
- Detectar e identificar pessoas conhecidas.
- Registrar hora e data da detecção.
- Salvar logs de eventos localmente (CSV ou banco local).
- Permitir visualização dos dados em tempo real via terminal.

### Requisitos Técnicos
- Python com DeepFace e OpenCV.
- Detecção e análise em tempo real com webcam.
- Armazenamento local (SQLite ou JSON).
- Log estruturado (arquivo .log e .csv).
- Backend simples com FastAPI.
- Frontend básico com HTML/CSS (renderizado via FastAPI).

---

## Fase 2: Banco de Dados e Interface Web

### Requisitos de Negócio
- Registrar histórico completo de detecções.
- Permitir consulta de logs por data/hora.
- Diferenciar pessoas conhecidas de desconhecidas.

### Requisitos Técnicos
- Integração com banco PostgreSQL ou SQLite (via ORM).
- API REST para consulta e inserção de registros.
- Interface web para listagem de eventos (React ou HTML + Jinja2).
- Tela de autenticação (básica) para acesso à interface.

---

## Fase 3: Deploy em Dispositivo Edge (Ex: Raspberry Pi)

### Requisitos de Negócio
- Rodar de forma autônoma em hardware local.
- Armazenar dados offline e sincronizar com a nuvem quando possível.

### Requisitos Técnicos
- Portar solução para rodar em Raspberry Pi (com webcam USB ou CSI).
- Otimizar uso de CPU e memória.
- Implementar fila de sincronização para registros offline.
- Serviço em background com reinício automático (Systemd ou Docker).

---

## Fase 4: Reconhecimento Facial com Identificação (Whitelisting)

### Requisitos de Negócio
- Reconhecer rostos específicos e associar nome.
- Criar cadastro de pessoas autorizadas.

### Requisitos Técnicos
- Treinar modelos de rosto com imagens cadastradas.
- Implementar banco de imagens (base de rostos).
- Ajustar lógica para associar nome ao rosto reconhecido.
- Interface de upload/cadastro de novos rostos.

---

## Fase 5: Integração com Notificações e Nuvem

### Requisitos de Negócio
- Notificar quando um rosto não reconhecido for detectado.
- Permitir acesso remoto aos dados via nuvem.

### Requisitos Técnicos
- Integração com serviços de notificação (Telegram, Email, WhatsApp via Twilio).
- Backend hospedado em nuvem (Render, Railway, AWS Free Tier).
- Comunicação segura (HTTPS, autenticação com token).
- Backup automático dos dados.

---

## Fase 6: Aprimoramento com Inteligência Artificial

### Requisitos de Negócio
- Melhorar precisão e performance de identificação.
- Reduzir falsos positivos/negativos.

### Requisitos Técnicos
- Substituir DeepFace por modelos otimizados (FaceNet, InsightFace).
- Utilizar embeddings e distância vetorial para verificação.
- Implementar cache de rostos para melhorar desempenho.