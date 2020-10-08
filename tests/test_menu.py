import pytest

from unittest import mock

from terminal_blog.blog import Blog
from terminal_blog.menu import Menu
from tests.test_constants import MockDatabase


class MockMenu(Menu):
    def __init__(self, database):
        self.database=database


@pytest.fixture
def test_menu():
    mock_menu = MockMenu(MockDatabase())
    mock_menu.user = "Foo"
    return mock_menu


class TestMenu:
    
    def test_verify_user_has_account_true(self, test_menu):
        test_menu.user = "Foo"
        assert True == test_menu.verify_user_has_account()

    def test_verify_user_has_account_false(self, test_menu):
        test_menu.database.find = lambda x, y: []
        assert False == test_menu.verify_user_has_account()
    
    @mock.patch("terminal_blog.blog.Blog.save_to_mongo", return_value=None)
    @mock.patch("builtins.input", return_value=True)
    def test_prompt_user_for_account(self, patched_input, patched_save_to_mongo, test_menu):
        test_menu.prompt_user_for_account()
        assert isinstance(test_menu.user_blog, Blog)
    
    @mock.patch("terminal_blog.blog.Blog.get_blog_from_mongo", return_value=True)
    def test_fetch_blog(self, patched_get_blog, test_menu):
        test_menu.database.find = lambda x, y: [{"blog_id": "1"}]
        test_menu.fetch_blog()
        assert True == test_menu.user_blog
