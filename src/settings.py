import os


class Settings:
    QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT = 6333
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EMBEDDING_DIMENSIONS = 1536
