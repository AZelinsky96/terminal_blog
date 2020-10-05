import pymongo as pmg

from terminal_blog.db_client_factory import MongoClient
from terminal_blog.post import Post

def main():
    mongo_client = MongoClient("local").create_client()
    post = Post("This is some content", "content", "Anthony")
    print(post)


if __name__ == "__main__":
    main()