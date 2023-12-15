DEMO_COLLECTION_NAME = "demo_collection"
EMBEDDING_MODEL = "text-embedding-ada-002"
CHAT_COMPLETION_MODEL = "gpt-3.5-turbo"

QNA_PROMPT = """
You are an assistant which answers questions based on the context provided.
Context:
{context}

If the context has answers, you should provide a concise answer to it.
If the question cannot be answered based on context,
you should say you dont have an answer followed by a joke in a sarcastic way.

Question: {question}
Answer:"""
