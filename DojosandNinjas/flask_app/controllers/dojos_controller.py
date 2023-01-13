from flask import Flask, render_template, request, redirect
from flask_app.models.dojo_model import Dojo           
from flask_app import app

#full crud routing
#/table_name/id/action
@app.route("/dojos")
def index():
    all_dojos = Dojo.get_all()   #method
    return render_template("index.html", all_dojos = all_dojos)

@app.route('/dojos/<int:id>/view')    
def get_one(id):
    data = {                          #or this way#
        'id':id
    }
    one_dojo = Dojo.get_one (data)
    return render_template("dojos_one.html",one_dojo = one_dojo)

@app.route("/dojos/create", methods = ["POST"])    
def create_dojo():
    Dojo.create(request.form)
    return redirect("/dojos")

