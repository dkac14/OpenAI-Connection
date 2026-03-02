# 🤖 OpenRouter + Python (Simple Setup)

Este proyecto es un ejemplo **simple y seguro** para conectarse a modelos de IA usando **OpenRouter** desde **Python**, sin exponer la API Key en el código.


## 📌 ¿Qué hace este proyecto?

- Se conecta a OpenRouter
- Usa un modelo de OpenAI (`gpt-4o-mini`)
- Lee la API Key desde un archivo `.env`
- Instala todas las dependencias desde `requirements.txt`


## 🛠️ Requisitos

- Python **3.8 o superior**
- Cuenta en OpenRouter
- API Key de OpenRouter


## 📦 Instalación

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/OpenAI-Connection.git
cd OpenAI-Connection
```

### 2️⃣ Instalar dependencias
Solo hacerlo una vez.
```bash
pip install -r requirements.txt
```

## 📄 requirements.txt
Contiene: 
- openai
- python-dotenv

## 🔐 Configuración de la API Key

1. En la raíz del proyecto crea un archivo llamado .env:

2. OPENROUTER_API_KEY=or-xxxxxxxxxxxxxxxxxxxx 

    ⚠️ **Nunca subas este archivo a GitHub**


3. Verifica .gitignore

    *Asegúrate de tener:*
    .env
