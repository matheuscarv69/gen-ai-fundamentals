import openai

# usando o novo modelo da openai usando o endpoint do groq compatível com openai
client = openai.OpenAI(base_url="https://api.groq.com/openai/v1")

responses = client.responses.create(
  model="llama-3.1-8b-instant",
  instructions="Responda de forma simples em apenas 1 paragrafo curto",
  input="O que é machine learning?"
)

print(responses.output)
print(responses.output_text)