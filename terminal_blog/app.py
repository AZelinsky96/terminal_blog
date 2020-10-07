import pymongo as pmg

from terminal_blog.blog import Blog
from terminal_blog.post import Post
from terminal_blog.db_client_factory import MongoClientFactory
from terminal_blog.mongo_dao import MongoDao


def main() -> None:
    mongo_client = MongoClientFactory("local").create_client()
    mongo_dao = MongoDao(mongo_client, "fullstack")
    blog = Blog.get_blog_from_mongo(
        blog_id='7613a5e8ed2d4a0f9a040bcbbd5365fc', database=mongo_dao
    )
    # blog.create_post()
    post = Post.get_post_from_mongo(
        post_id='0f956cb6e46749a982412056d17b86ee', database=mongo_dao
    )
    print(post)


if __name__ == "__main__":
    main()