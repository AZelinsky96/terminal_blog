from datetime import datetime
from uuid import uuid4

class Posts(object):
    
    COLLECTION = "posts"


    def __init__(self, database: object):
        self.database = database

    def __repr__(self) -> str:
        return f"<Post object attrs: blog_id='{self.database}', collection='{self.collection}'"

    def create_json(
        self, blog_id: int, post_id: int, author: str, content: str,
        title:str, date_created: datetime) -> dict:
        return {
            "blog_id": blog_id,
            "post_id": post_id,
            "author": author,
            "content": content,
            "title": title,
            "date_created": datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        }

    def save_to_mongo(
        self, blog_id:int, author: str, content:str, title:str,
        post_id: int=-99, date_created: datetime=datetime.now()) -> None:
        self.database.insert(
            collection=self.COLLECTION, data=self.create_json(
                blog_id=blog_id, post_id=uuid4().int if post_id == -99 else post_id.hex,
                author=author, content=content, title=title
            )
        )

    def find_post_from_mongo(self, post_id: int) -> dict:
        return self.database.find_one(self.COLLECTION, {"post_id": post_id})

    def find_blog_from_mongo(self, blog_id: int) -> list:
        return [post for post in self.database.find(self.COLLECTION, {"blog_id": blog_id})]

    def search_mongo(self, **kwargs) -> list:
        return [post for post in self.database.find(self.COLLECTION, kwargs)]