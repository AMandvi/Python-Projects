from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model        ##since we are in model ao we will bring in whole module
import re

class Party:
    def __init__(self,data) -> None:
        self.id = data['id']
        self.what = data['what']
        self.location = data['location']
        self.date = data['date']
        self.all_ages = data['all_ages']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    
    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO parties (what, location, date, all_ages, description, user_id)
        VALUES (%(what)s, %(location)s, %(date)s, %(all_ages)s, %(description)s, %(user_id)s)
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM parties JOIN users ON parties.user_id = users.id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all_parties = []            ##list
        if results:              
            for row in results:
                this_party = cls(row)                 #party instance 
                user_data = {                         #target all the user data
                    **row,                             #copying in the row   and getting ambiguous field/shared between the two
                    'id' : row['users.id'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at']
                }
                this_user = user_model.User(user_data)   #user class instance with user data
                this_party.planner = this_user           #brand new attribute(planner) is equal to this_user
                all_parties.append(this_party)           #then we will put this_party in the list of all_parties
        return all_parties                               #return that list. will get empty list or all the parties
                                                        #whole user object into the atrribute planner
    @classmethod
    def get_one(cls,data):
        query = """
        SELECT * FROM parties JOIN users ON parties.user_id = users.id
        WHERE parties.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        print (results)
        if results:
            row = results[0]
            this_party = cls(row)
            user_data = {                         #target all the user data
                    **row,                             #copying in the row   and getting ambiguous field/shared between the two
                    'id' : row['users.id'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at']
                }
            this_user = user_model.User(user_data)   #user class instance with user data
            this_party.planner = this_user
            return this_party
        return False

    

    @classmethod
    def update(cls,data):
        query= """
        UPDATE parties SET what = %(what)s, location = %(location)s,
        description = %(description)s, date = %(date)s,
        all_ages = %(all_ages)s
        WHERE parties.id = %(id)s;   
    """
        return connectToMySQL(DATABASE).query_db(query,data)        

    @classmethod
    def delete(cls,data):
        query = """
        DELETE FROM parties WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validator(form_data):
        is_valid = True
        print(form_data)
        if len(form_data['what']) < 1:
            flash("what required")
            is_valid = False
        if len(form_data['location']) < 1:
            flash("location required")
            is_valid = False
        if len(form_data['date']) < 1:
            flash("date required")
            is_valid = False
        if len(form_data['description']) < 1:
            flash("description required")
            is_valid = False
        if "all_ages" not in form_data:                       #since this will not make the key will only make on or nothing
            flash("all ages required")
            is_valid = False
        return is_valid