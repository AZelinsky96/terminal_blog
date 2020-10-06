

class MongoDao(object):

    def __init__(self, client, database):
        self.client = client
        self.database = client[f'{database}']
    
    def __repr__(self):
        return (
            f"<MongoDao object: database='{self.database}'"
        )
    
    def insert(self, collection, data):
        try:
            self.database[collection].insert(data)
        except Exception as e:
            raise Exception(f"Error occured during insert operation: {e}.")
    
    def find(self, collection, query):
        return self.database[collection].find(query)
    
    def find_one(self, collection, query):
        return self.database[collection].find_one(query)