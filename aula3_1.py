from openai import OpenAI

from aula1_2 import feedbacks

openai_api_key = "sua-chave-aqui"

client = OpenAI(api_key=openai_api_key)

def analisar_sentimentos(feedbacks):

    comentarios_formatados = "\n".join([f"- {feedback.comentario}" for feedback in feedbacks])

    prompt = f"""
                Analise os seguintes comentários e os classifique em Positivo, Neutro e Negativo:
                {comentarios_formatados}"""

    respostaAPI = client.chat.completions.create(
    model="gpt-4o-mini",
    max_tokens=20,
    messages=[
        {
            "role": "system",
            "content": "Você é um modelo de análise de sentimentos com foco em feedbacks sobre experiências educacionais."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

    return respostaAPI.choices[0].message.content

insigths = analisar_sentimentos(feedbacks)
print(insigths)