from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import dojo_model       

class Ninja:
    def __init__(self,data) :
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod      
    def create(cls,data):
        query = """
            INSERT INTO ninjas (first_name,last_name,dojo_id,age)
            VALUES (%(first_name)s,%(last_name)s, %(dojo_id)s,%(age)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM ninjas JOIN dojos
            ON dojos.id = ninjas.dojo_id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all_ninjas = []
        if results:
            for row in results:
                ninja_instance = cls(row)   ####
                dojo_data = {
                    **row,
                    "id": row['dojos.id'],
                    "created_at": row['dojos.created_at'],
                    "updated_at": row['dojos.updated_at']
                }
                dojo_instance = dojo_model.Dojo(dojo_data)
                ninja_instance.recipient = dojo_instance 
                all_ninjas.append(ninja_instance)
        return all_ninjas

    @classmethod 
    def get_one(cls,data):
        query = """
            SELECT * FROM ninjas JOIN dojos
            ON dojos.id = ninjas.dojo_id 
            WHERE ninjas.id = %(id)s          
        """

        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if results:
            ninja_instance  = cls(results[0])
            row = results[0]
            dojo_data = {
                    **row,
                    "id": row['dojos.id'],
                    "created_at": row['dojos.created_at'],
                    "updated_at": row['dojos.updated_at']
                }
            dojo_instance = dojo_model.Dojo(dojo_data)
            ninja_instance.recipient = dojo_instance
            return ninja_instance
            return False