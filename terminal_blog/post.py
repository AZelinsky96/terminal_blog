from datetime import datetime
from uuid import uuid4

class Post(object):
    
    COLLECTION = "posts"

    def __init__(
        self, blog_id: int, author: str, content: str,
        title: str, database: object, post_id: str=None) -> None:
        self.blog_id = blog_id
        self.author = author
        self.content = content
        self.title = title
        self.database = database
        self.post_id = uuid4().hex if post_id is None else post_id


    def __repr__(self) -> str:
        return f"<Post object attrs: blog_id='{self.blog_id}, 'post_id='{self.post_id}', title='{self.title}'"

    def create_json(self) -> dict:
        return {
            "blog_id": self.blog_id,
            "post_id": self.post_id,
            "author": self.author,
            "content": self.content,
            "title": self.title,
            "date_created": datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        }

    def save_to_mongo(self) -> None:
        self.database.insert(
            collection=self.COLLECTION, data=self.create_json()
        )

    def search_for_posts_in_mongo(self, **kwargs) -> list:
        return [post for post in self.database.find(self.COLLECTION, kwargs)]

    @classmethod
    def get_post_from_mongo(self, post_id: int, database: database) -> dict:
        post_data = database.find_one(
            collection=self.COLLECTION, query={"post_id": post_id}
        )
        return cls(
            blog_id=post_data['blog_id'],
            post_id=post_data['post_id'],
            author=post_data['author'],
            content=post_data['content'],
            title=post_data['title'],
            database=database
        )
        self.database.find_one(self.COLLECTION, {"post_id": post_id})
