from dotenv import load_dotenv      # Carga variables de entorno desde .env
import os                           # Permite acceder a variables del sistema
from openai import OpenAI           # Cliente compatible con OpenAI / OpenRouter

# Lee el archivo .env
load_dotenv()                       

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),  # Obtiene la API Key de OpenRouter
    base_url="https://openrouter.ai/api/v1"   # Endpoint de OpenRouter
)

response = client.chat.completions.create(
    model="openai/gpt-4o-mini",     # Modelo elegido desde OpenRouter
    messages=[
        {"role": "user", "content": "How to learn ML and AI using Python?"}
    ]
)

print(response.choices[0].message.content)    # Imprime la respuesta del modelo