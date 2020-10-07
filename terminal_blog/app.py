import pymongo as pmg

from terminal_blog.blog import Blog
from terminal_blog.post import Post
from terminal_blog.menu import Menu
from terminal_blog.db_client_factory import MongoClientFactory
from terminal_blog.mongo_dao import MongoDao


def main() -> None:
    mongo_client = MongoClientFactory("local").create_client()
    mongo_dao = MongoDao(mongo_client, "fullstack")
    menu = Menu(database=mongo_dao)
    menu.run_menu()


if __name__ == "__main__":
    main()