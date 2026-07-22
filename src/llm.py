import ollama


def ask_ai(question, context):

    response = ollama.chat(

        model="qwen2.5-coder:3b",

        messages=[

            {
                "role": "system",
                "content":
                """
                Você é um assistente que responde
                usando somente o contexto fornecido.
                """
            },

            {
                "role": "user",
                "content":
                f"""
                Contexto:

                {context}


                Pergunta:

                {question}
                """
            }

        ]
    )


    return response["message"]["content"]
