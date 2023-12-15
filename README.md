# pycon2023VirtualAssistantDemo
Virtual Assistant 2.0 Demo for GDG Devfest

# SETUP
- Setup your virtual environment.
- install requirements `pip install -r requirements.txt`
- This repo uses, qdrant DB as vector DB, and open AI APIs for LLM calls.
- Setup a Qdrant DB [locally](https://qdrant.tech/) or [qdrant cloud](https://cloud.qdrant.io/) cloud they have a free tier.
- Setup an openAI account and create an API key.


# HOW TO USE

- Set following env variables:
```bash
export QDRANT_HOST=QDRANT_HOST
export QDRANT_API_KEY=QDRANT_API_KEY
export OPENAI_API_KEY=OPENAI_API_KEY
```

- Run main.py, `python3 main.py`