

class Post(object):
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return (f"<Post object attrs: title='{self.title}', content='{self.content}',"
                f" author='{self.author}'>")