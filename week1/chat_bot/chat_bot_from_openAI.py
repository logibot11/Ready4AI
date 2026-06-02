
# Autor uczący się: Jarosław Krefft
# Data utworzenia: 02.06.2026
# Nazwa i wersja programu: chat_bot_from_openAI.py
# kod pobrany ze strony https://developers.openai.com/api/docs/guides/conversation-state
# Open Ai - Developers 
# w kodzie jest przekazywane id rozmowy ale jednokrotnie bez pętli
 
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="tell me a joke",
)

print(response.output_text)

second_response = client.responses.create(
    model="gpt-4.1-mini",
    previous_response_id = response.id,
    input = [{"role": "user", "content" : "explain why this is funny"}],
)

print(second_response.output_text)

