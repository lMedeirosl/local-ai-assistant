from document_loader import load_documents
from llm import ask_ai


documents = load_documents()


while True:

    question = input("\nPergunta: ")


    answer = ask_ai(
        question,
        documents
    )


    print("\nResposta:")
    print(answer)

