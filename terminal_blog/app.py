import pymongo as pmg

from terminal_blog.post import Posts
from terminal_blog.db_client_factory import MongoClientFactory
from terminal_blog.mongo_dao import MongoDao

def main():
    mongo_client = MongoClientFactory("local").create_client()
    mongo_dao = MongoDao(mongo_client, "fullstack")
    posts = Posts(mongo_dao)
    # posts.save_to_mongo(
    #     blog_id=1,
    #     author="Anthony",
    #     content="This is my first post.",
    #     title="Primary Post",
    # )


if __name__ == "__main__":
    main()