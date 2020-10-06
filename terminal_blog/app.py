import pymongo as pmg

from terminal_blog.blog import Blog
from terminal_blog.post import Post
from terminal_blog.db_client_factory import MongoClientFactory
from terminal_blog.mongo_dao import MongoDao


def main() -> None:
    mongo_client = MongoClientFactory("local").create_client()
    mongo_dao = MongoDao(mongo_client, "fullstack")
    blog = Blog(
        author="Anthony", blog_title="Anthony's Blog",
        description="My first blog", database=mongo_dao
    )
    blog.create_post()


if __name__ == "__main__":
    main()