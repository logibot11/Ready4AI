# Autor uczący się: Jarosław Krefft
# Data utworzenia: 13.05.2026
# Nazwa i wersja programu: python_api_flask.py 
# Przykład użycia modelu openAI .

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5.4-mini",
    input="Wymień 5 pierwiastków najczęściej wystepujcych w urządzeniach elektronicznych"
)

print(response.output_text)
