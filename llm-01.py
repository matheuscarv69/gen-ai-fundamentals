from groq import Groq

client = Groq()

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": "Atue como um especialista em machine learning."},
        {"role": "user", "content": "De forma simples, o que é machine learning?"},
    ],
    # temperature: controla a aleatoriedade das respostas (0 = determinístico, 2 = muito criativo)
    temperature=1,
    # top_p: controla a diversidade via nucleus sampling (0.1 = conservador, 1 = considera todos os tokens)
    top_p=1,
)

print(response.choices[0].message.content)
