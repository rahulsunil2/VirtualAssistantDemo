import openai
from src.settings import Settings
from src.constants import EMBEDDING_MODEL, CHAT_COMPLETION_MODEL

openai.api_key = Settings.OPENAI_API_KEY


class OpenAIClient:
    def create_embedding(self, text: str) -> list[float]:
        response = openai.Embedding.create(model=EMBEDDING_MODEL, input=text.strip())
        return response["data"][0]["embedding"]  # type: ignore

    def create_chat_completion(
        self, messages: list[dict], model: str = CHAT_COMPLETION_MODEL
    ) -> str:
        response = openai.ChatCompletion.create(
            model=model, temperature=0, messages=messages
        )
        return response["choices"][0]["message"]["content"]  # type: ignore
