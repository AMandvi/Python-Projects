from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM users;
        """
        results = connectToMySQL(DATABASE).query_db (query)
        print(results)
        all_users = []
        for one_row in results:
            this_user_instance = cls(one_row)
            all_users.append(this_user_instance)
        return all_users

    @classmethod
    def get_one(cls,data):
        query = """
            SELECT * FROM users WHERE users.id =  %(id)s ;
        """
        results = connectToMySQL(DATABASE).query_db (query, data)
        print(results)
        if results:
            user_instance = cls(results[0])
            return user_instance
    @classmethod
    def create(cls,data):
        query = """
            INSERT INTO users (first_name,last_name,email)
            VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        print(query)
        return connectToMySQL(DATABASE).query_db(query,data)    

    @classmethod
    def update(cls,data):
        query = """
            UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s , email = %(email)s 
            WHERE users.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db (query,data)

    @classmethod
    def delete(cls,data):
        query = """
            DELETE FROM users WHERE users.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db (query,data)    