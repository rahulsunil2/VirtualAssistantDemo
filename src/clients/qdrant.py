from qdrant_client import QdrantClient
from qdrant_client.models import Distance, Filter, PointStruct, VectorParams
from src.settings import Settings
from typing import Optional


class QClient:
    def __init__(self):
        self.client = QdrantClient(
            host=Settings.QDRANT_HOST,
            port=Settings.QDRANT_PORT,
            api_key=Settings.QDRANT_API_KEY,
        )

    def is_collection_present(self, collection: str) -> bool:
        existing_collections = self.client.get_collections().collections
        for existing_collection in existing_collections:
            if existing_collection.name == collection:
                return True

        return False

    def create_collection(self, collection: str):
        self.client.create_collection(
            collection_name=collection,
            vectors_config=VectorParams(
                size=Settings.EMBEDDING_DIMENSIONS,
                distance=Distance.COSINE,
            ),
        )

    def recreate_collection(self, collection: str):
        if self.is_collection_present(collection):
            self.client.recreate_collection(
                collection_name=collection,
                vectors_config=VectorParams(
                    size=Settings.EMBEDDING_DIMENSIONS,
                    distance=Distance.COSINE,
                ),
            )
        else:
            self.create_collection(collection)

    def upsert_many(
        self, collection: str, vectors: list[tuple[int, list[float], dict]]
    ):
        self.client.upsert(
            collection_name=collection,
            points=[
                PointStruct(id=int(vector_id), vector=values, payload=metadata)
                for vector_id, values, metadata in vectors
            ],
        )

    def query(
        self,
        collection: str,
        query_embedding: list[float],
        top_n: int,
        filters: Optional[Filter] = None,
    ) -> list[tuple[int, float, dict]]:
        response = self.client.search(
            collection_name=collection,
            query_vector=query_embedding,
            query_filter=filters,
            limit=top_n,
        )

        return [(int(item.id), item.score, item.payload or {}) for item in response]
