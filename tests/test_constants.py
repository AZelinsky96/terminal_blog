class MockDatabase:

    def find(self, *args, **kwargs):
        return [num for num in range(10)]

    def find_one(self, *args, **kwargs):
        return {
            "author": "Anthony",
            "blog_title": "Test",
            "description": "Test desc",
            "blog_id": "1"
        }