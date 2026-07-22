import os


def load_documents():

    folder = "documents"

    documents = []


    for file in os.listdir(folder):

        path = os.path.join(folder, file)


        with open(path, "r", encoding="utf-8") as f:

            content = f.read()

            documents.append(content)


    return "\n".join(documents)
