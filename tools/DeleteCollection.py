
import os
import chromadb

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
                             settings=Settings(#chroma_client_auth_provider="chromadb.auth.basic.BasicAuthClientProvider",
                                               chroma_client_auth_credentials=f"{ChromadbUser}:{ChromadbPassword}"))

client.delete_collection(name="questionAutoEnbeddingCosine")