from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

resposta = cliente.chat.completions.create(
    messages = [
        {
            "role": "system",
            "content": "Listar apenas os nomes dos produtos, sem considerar descrição."
        },
        {
            "role": "user",
            "content": "Liste 2 produtos sustentáveis"
        }
    ],
    model="gpt-3.5-turbo-0125"
)

print(resposta.choices[0].message.content)
