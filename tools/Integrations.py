
import os
import chromadb
import chromadb.utils.embedding_functions as embedding_functions

from chromadb.config import Settings
from dotenv import load_dotenv

load_dotenv()

ChromadbIP = os.getenv('ChromadbIP')
ChromadbPort = os.getenv('ChromadbPort')
ChromadbUser = os.getenv('ChromadbUser')
ChromadbPassword = os.getenv('ChromadbPassword')

ServerIP = os.getenv('ServerIP')
OpenAiPort = os.getenv('OpenAiPort')

print(f"ServerIP: {ServerIP}")
print(f"OpenAiPort: {OpenAiPort}")

client = chromadb.HttpClient(host= ChromadbIP,
                             port= ChromadbPort,
                             settings=Settings(chroma_client_auth_provider="chromadb.auth.basic.BasicAuthClientProvider",
                                               chroma_client_auth_credentials=f"{ChromadbUser}:{ChromadbPassword}"))

api_base=f"http://{ServerIP}:{OpenAiPort}/v1"

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_base=api_base,
                api_key="no need key",
                model_name="resetful api"
            )

collection = client.get_or_create_collection(name="integrations", embedding_function=openai_ef)
# collection = client.create_collection(name="integrations", embedding_function=openai_ef)
# collection = client.get_collection(name="name", embedding_function=openai_ef)

collection.query(Document=[], n_results=1)

result = openai_ef(input=["Good night", "How are you?"])

collection.add(documents=["Good night", "How are you?"], ids=["1", "2"])
print(result)
