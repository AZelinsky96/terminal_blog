import pytest

from unittest.mock import patch
from terminal_blog.db_client_factory import MongoClientFactory


def mock_create_local_client_error():
    raise ValueError

class TestDBClientFactory:

    @patch("terminal_blog.db_client_factory.create_local_client", return_value="LocalClient")
    def test_create_client_pass(self, create_local_client_patch):
        with patch("terminal_blog.db_client_factory.CONNECTIONS", {"local": create_local_client_patch}):
            test_mongo_client = MongoClientFactory("local")
            assert create_local_client_patch() == test_mongo_client.create_client()


    def test_create_client_fail(self):
        with patch("terminal_blog.db_client_factory.CONNECTIONS", {"local": mock_create_local_client_error}):
            test_mongo_client = MongoClientFactory("local")
            with pytest.raises(Exception):
                test_mongo_client.create_client()
