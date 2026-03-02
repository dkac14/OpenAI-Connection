from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENROUTER_API_KEY"),
                base_url = "https://openrouter.ai/api/v1"
                )

max_completion_tokens = 500
# Texto original que será resumido
text = """Inclusive education aims to ensure that all students, regardless of their abilities or backgrounds, have equal access to learning opportunities.
It values diversity as a strength and promotes respect, participation, and equity in the classroom.
Teachers play a key role by adapting teaching strategies, materials, and assessments to meet diverse needs.
Family involvement and collaboration with support professionals strengthen the learning process.
An inclusive classroom fosters empathy, cooperation, and social development among students.
Flexible methodologies help reduce learning barriers and enhance student engagement.
Inclusive practices benefit not only students with special needs, but the entire educational community.
Creating a positive classroom climate is essential for effective inclusion.
Ongoing teacher training supports the implementation of inclusive strategies.
Ultimately, inclusive education contributes to a more just and equitable society."""

# Prompt que se envía al modelo
# Se le indica claramente la tarea (resumir en 5 puntos clave)
# y luego se adjunta el texto a resumir
prompt = f"Summarize the following text into 5 clear and concise key points. Focus on the main ideas and avoid unnecessary details. Use simple and precise language, {text}"

# Llamada a la API de OpenAI (vía OpenRouter)
response = client.chat.completions.create(
    model = "openai/gpt-4o-mini",
    messages = [{"role": "user", "content": prompt}],
    max_completion_tokens = max_completion_tokens
)

input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = max_completion_tokens
# Calculate cost
cost = (input_tokens * input_token_price + output_tokens * output_token_price)

print(f"Estimated cost: ${cost}\n")


# Imprime el contenido del mensaje generado por el modelo
print(response.choices[0].message.content)