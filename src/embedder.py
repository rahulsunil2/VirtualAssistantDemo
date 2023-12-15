from src.clients.qdrant import QClient
from src.clients.openai import OpenAIClient
from langchain.text_splitter import CharacterTextSplitter
from src.logger import logger


class Embedder:
    vector_db_client = QClient()
    openai_client = OpenAIClient()

    def embed_information(self, collection: str, text: str, name: str):
        """Embeds information into the vector database

        Args:
            collection (str): Collection to store the information
            text (str): Information to embed
        """
        logger.info("Recreating collection...")
        self.vector_db_client.recreate_collection(collection=collection)
        logger.info("Splitting text into chunks...")
        text_chunks = CharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
        ).split_text(text)
        logger.info(f"{len(text_chunks)} number of chunks found")
        index = 0
        vectors: list[tuple[int, list[float], dict]] = []
        for text_chunk in text_chunks:
            logger.debug(f"Calculating embedding for the text chunk: {index}")
            logger.debug(f"Text chunk: {text_chunk}")
            logger.debug("----------------------")
            embedding = self.openai_client.create_embedding(text_chunk.strip())
            vectors.append((index, embedding, {"content": text_chunk, "name": name}))
            index += 1

        self.vector_db_client.upsert_many(
            collection=collection,
            vectors=vectors,
        )
        logger.info("Successfully indexed information!")
