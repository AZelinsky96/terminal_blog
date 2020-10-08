import pytest

from terminal_blog.blog import Blog
from tests.test_constants import MockDatabase
    

@pytest.fixture
def blog_object():
    return Blog(
            blog_id="1",
            author="Anthony",
            blog_title="Test",
            description="Test desc",
            database=MockDatabase()
        )


class TestBlog:
    
    def test_find_posts_from_blog(self, blog_object):
        expected = [num for num in range(10)]
        assert expected == blog_object.find_posts_from_blog()
    
    def test_create_json(self, blog_object):
        expected_data = {
            "blog_id": "1",
            "author": "Anthony",
            "blog_title": "Test",
            "description": "Test desc"
        }
        blog_data = blog_object.create_json()
        for key in expected_data.keys():
            assert expected_data[key] == blog_data[key]

    def test_get_blog_from_mongo(self, blog_object):
        test_blog = blog_object.get_blog_from_mongo("1", MockDatabase())
        assert isinstance(test_blog, Blog)