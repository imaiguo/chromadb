
import os
import chromadb

from chromadb.config import Settings
from dotenv import load_dotenv
from loguru import logger

os.environ["CHROMA_CLIENT_AUTH_PROVIDER"]="chromadb.auth.basic_authn.BasicAuthClientProvider"

class ChromaDB(object):
    
    def __init__(self) -> None:
        self.laodConfig()
        self.getClient()

    def laodConfig(self):
        load_dotenv()
        self.ChromadbIP = os.getenv('ChromadbIP')
        self.ChromadbPort = os.getenv('ChromadbPort')
        self.ChromadbUser = os.getenv('ChromadbUser')
        self.ChromadbPassword = os.getenv('ChromadbPassword')

        print(f"ChromaDBIP: {self.ChromadbIP}")
        print(f"ChromaDBPort: {self.ChromadbPort}")
        print(f"ChromaDBUser: {self.ChromadbUser}")
        print(f"ChromaDBPassword: {self.ChromadbPassword}")

    def getClient(self):
        self.dbClient = chromadb.HttpClient(host= self.ChromadbIP,
                             port= self.ChromadbPort,
                             settings=Settings(# chroma_client_auth_provider="chromadb.auth.basic.BasicAuthClientProvider",
                                               chroma_client_auth_credentials=f"{self.ChromadbUser}:{self.ChromadbPassword}")
                            )

        result = self.dbClient.heartbeat()
        logger.debug(f"result ->{result}")
        # this should work with or without authentication - it is a public endpoint
        version = self.dbClient.get_version()
        logger.debug(f"version ->{version}")

    def getCollection(self):
        result = self.dbClient.list_collections()
        logger.debug(f"collections list->{result}")
        return result

info = ChromaDB()

collections = info.getCollection()
for co in collections:
    print(f"collections -> Name:{co.name}\t count:{co.count()}")
