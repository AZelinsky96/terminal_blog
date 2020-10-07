from terminal_blog.blog import Blog

class Menu(object):

    def __init__(self, database):
        self.database = database
        self.check_for_user()

    def check_for_user(self) -> None:
        self.user = input("Please enter your username: ")
        if self.verify_user_has_account():
            print(f"Welcome back: {self.user}")
        else:
            print("No user found, please create your blog!")
            self.prompt_user_for_account()

    def verify_user_has_account(self):
        user_result = [user for user in self.database.find("blogs", {"author": self.user})]
        self.fetch_blog()
        return True if user_result else False
    
    def prompt_user_for_account(self):
        blog = Blog(
            author=self.user, blog_title= input("Enter blog title: "),
            description=input("Enter blog description: "), database=self.database
        )
        blog.save_to_mongo()
        self.user_blog = blog
 
    def fetch_blog(self):
        blog = [blog for blog in self.database.find("blogs", {"author": self.user})][0]
        self.user_blog = Blog.get_blog_from_mongo(
            blog_id=blog['blog_id'], database=self.database
        )

    def run_menu(self):
        read_or_write = self.check_if_read_or_write()
        self.run_menu_helper(read_or_write)
    
    def check_if_read_or_write(self):
        read_or_write = input("Would you like to read (R) or write (W)?: ")
        while read_or_write.lower() not in ("r", "w"):
            read_or_write = input("Invalid entry! Please enter (R) to read or (W) to write: ")
        return read_or_write
    
    def run_menu_helper(self, read_or_write):
        if read_or_write.lower() == "r":
            self.read_blogs()
        else:
            self.write_to_blog()
    
    def read_blogs(self):
        self.list_blogs()
        self.view_blogs()
    
    def list_blogs(self):
        blogs = self.database.find("blogs", {})
        for blog in blogs:
            print(
                f"Blog Id: {blog['blog_id']}, Title: {blog['blog_title']}, Author: {blog['author']}"
            )
    
    def view_blogs(self):
        blog_to_view = input("Enter blog id you'd want to view: ")
        blog = Blog.get_blog_from_mongo(
            blog_id=blog_to_view, database=self.database
        )
        for post in blog.find_posts_from_blog():
            print(
                f"\nDate: {post['date_created']}\nTitle: {post['title']}\nAuthor: {post['author']}\nContent:\n{post['content']}\n"
            )

    def write_to_blog(self):
        self.user_blog.create_post()