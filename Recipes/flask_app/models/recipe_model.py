from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model        ##since we are in model ao we will bring in whole module
import re

class Recipe:
    def __init__(self,data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date = data['date']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO recipes (name, description, instruction, date, under, user_id)
        VALUES (%(name)s, %(description)s, %(instruction)s, %(date)s, %(under)s, %(user_id)s);
        """    
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []                #list
        if results:
            for row in results:
                this_recipe = cls(row)                 #recipe instance 
                user_data = {                           #target all the user data
                    **row,                               #copying in the row   and getting ambiguous field/shared between the two
                    'id' : row['user_id'],
                    'created_at' :row['users.created_at'],
                    'updated_at' : row['users.updated_at']
                }
                this_user = user_model.User(user_data)   #user class instance with user data
                this_recipe.planner = this_user           #brand new attribute(planner) is equal to this_user
                all_recipes.append(this_recipe)
        return all_recipes 

    @classmethod
    def get_one(cls,data):
        query = """
        SELECT * FROM recipes JOIN users ON recipes.user_id = users.id
        WHERE recipes.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if results:
            row = results[0]
            this_recipe = cls(row)
            user_data = {
                **row,
                'id' : row['users.id'],
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at']
            }
            this_user = user_model.User(user_data)              #user class instance with user data
            this_recipe.planner = this_user
            return this_recipe
        return False 

    @classmethod
    def update(cls,data):
        query = """
        UPDATE recipes SET name = %(name)s, description = %(description)s,instruction = %(instruction)s,
        date = %(date)s, under = %(under)s WHERE recipes.id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = """
        DELETE FROM recipes WHERE id = %(id)s;
        """ 
        return connectToMySQL(DATABASE).query_db(query,data)           


    @staticmethod
    def validator(form_data):
        is_valid = True
        print(form_data)
        if len(form_data['name']) < 1:
            flash("name required")
            is_valid = False
        if len(form_data['description']) < 1:
            flash("description required")
            is_valid = False
        if len(form_data['date']) < 1:
            flash("date required")
            is_valid = False
        if len(form_data['instruction']) < 1:
            flash("instructions required")
            is_valid = False
        if "under" not in form_data:                       #since this will not make the key will only make on or nothing
            flash("Under 30 min. ckeckbox required")
            is_valid = False
        return is_valid