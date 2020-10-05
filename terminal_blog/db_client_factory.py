
from terminal_blog.constants import uri
from pymongo import MongoClient


def create_local_client() -> MongoClient:
    return pmg.MongoClient(uri)


class MongoClient(object):

    CONNECTIONS = {
        "local": create_local_client
    }

    def __init__(self, connection_type: str):
        self.connection_type = connection_type

    def create_client(self) -> MongoClient:
        try:
            return self.CONNECTIONS[self.connection_type]
        except KeyError:
            raise KeyError("Unsupported Connection Type")