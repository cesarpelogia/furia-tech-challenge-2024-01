# 🏎️ FURIA Tech Challenge 2024

**Desenvolvedor:** Cesar Pelogia | [LinkedIn](https://www.linkedin.com/in/cesar-augusto-anselmo-pelogia-truyts-94a08a268/) | [GitHub](https://github.com/cesarpelogia)

---

## 🎯 Descrição
Este repositório contém a entrega dos desafios técnicos do processo seletivo para Assistente de Engenharia de Software na FURIA Tech.

Foram desenvolvidos dois projetos:

Challenge #1 - Experiência Conversacional FURIA: Um chatbot para fãs do time de CS da FURIA.

O repositório contém:

- Código-fonte organizado em pastas separadas.
- Documentação detalhada para cada projeto.
- Vídeos demonstrativos das aplicações em funcionamento.

🚀 Desenvolvido com foco em criatividade, usabilidade e melhoria contínua (Kaizen).

---

## ⚡ Projetos
- **Challenge #1**: Experiência Conversacional para fãs da FURIA

---

## 🛠️ Tecnologias
- Python 3
- API do Telegram (via biblioteca TeleBot)
- Gerenciamento de variáveis de ambiente (via `python-dotenv`)

---

## 🤖 Teste o Bot

Você pode testar o bot diretamente no Telegram clicando no link abaixo:

[👉 Acesse o bot aqui](https://t.me/hermesFuriaBot)

Ou procure por `@hermesFuriaBot` no Telegram.

---

## 🚀 Como Rodar

```bash
# Clone o repositório
git clone https://github.com/seuusuario/furia-challenge-chatbot.git
cd furia-challenge-chatbot

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python challenge-1-experiencia-conversacional/src/main.py
```

---

## ⚙️ Configuração

1. O arquivo `.env.example` já contém uma chave de API configurada para o bot personalizado.
2. Copie o arquivo `.env.example` como `.env`:

```bash
cp .env.example .env  # Linux/Mac
copy .env.example .env  # Windows
```

3. O bot já estará pronto para uso com as configurações personalizadas.

> **Nota:** A chave de API fornecida é temporária e será desativada após o processo de avaliação.

---

### 🔑 Como obter uma chave de API do Telegram

1. Abra o Telegram e procure por "BotFather".
2. Inicie uma conversa com o BotFather e envie o comando `/newbot`.
3. Siga as instruções para criar um novo bot.
4. Após criar o bot, o BotFather fornecerá um token de API. Use esse token no arquivo `.env` como o valor de `TELEGRAM_TOKEN`.