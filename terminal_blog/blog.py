from uuid import uuid4

from terminal_blog.post import Post


class Blog(object):

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

    def find_posts(self):
        pass

    def save_to_mongo(self):
        pass


    