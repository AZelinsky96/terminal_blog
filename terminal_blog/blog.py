from datetime import datetime
from uuid import uuid4

from terminal_blog.post import Post


class Blog(object):

    COLLECTION = "blogs"

    def __init__(
        self, author: str, blog_title: str, description: str,
        database: object, blog_id: str=None,
        ) -> None:
        self.author = author
        self.blog_title = blog_title
        self.description = description
        self.database = database
        self.blog_id = uuid4().hex if blog_id is None else blog_id


    def create_post(self) -> None:
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        post = Post(
            blog_id=self.blog_id, author=self.author, content=content, 
            title=title, database=self.database)
        post.save_to_mongo()

    def find_posts_from_blog(self) -> list:
        return [post for post in self.database.find("posts", {"blog_id": self.blog_id})]

    def save_to_mongo(self):
        self.database.insert(
            collection=self.COLLECTION, data=self.create_json()
            )

    def create_json(self):
        return {
            "blog_id": self.blog_id,
            "author": self.author,
            "title": self.title,
            "description": self.description,
            "date_created": datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        }

    @classmethod
    def get_blog_from_mongo(cls, blog_id: str, database: object) -> Blog:
        blog_data = database.find_one(
            collection="blogs",
            query={"blog_id": blog_id}
        )
        return cls(
            author=blog_data['author'],
            title=blog_data['title'],
            description=blog_data["description"],
            database=database,
            blog_id=blog_data['blog_id']
        )
    