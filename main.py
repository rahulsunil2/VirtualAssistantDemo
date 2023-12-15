import os
from src.embedder import Embedder
from src.assistant import Assistant
from src.constants import DEMO_COLLECTION_NAME


def index_documents():
    # read all text files in the documents folder

    for file_name in os.listdir("./documents"):
        with open(f"./documents/{file_name}", "r") as f:
            text = f.read()

        print(f"Indexing document: {file_name}")
        Embedder().embed_information(
            collection=DEMO_COLLECTION_NAME,
            text=text,
            name=file_name,
        )


def query_documents():
    while True:
        question = input("\n\nAsk a question, (Type 'exit' to exit).\n\nQuestion: ")
        if question.lower().strip() == "exit":
            break

        answer = Assistant().get_answer(question=question)
        print(f"Answer: {answer}")
        print("\n\n\n")


def main():
    print("\n\nWhat would you like to do?\n1. Index documents\n2. Query documents")
    choice = input("Enter your choice: ")
    if choice == "1":
        index_documents()
    elif choice == "2":
        query_documents()


if __name__ == "__main__":
    main()
