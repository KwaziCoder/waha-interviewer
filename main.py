import os
import dotenv
from langchain_community.llms import YandexGPT

dotenv.load_dotenv()

llm = YandexGPT(
    api_key=os.getenv("LLM_AUTH_KEY"),
    folder_id=os.getenv("LLM_FOLDER"),
    model_name="yandexgpt-lite",
    temperature=0.7
)

result = llm("Привет!")

print(result)
