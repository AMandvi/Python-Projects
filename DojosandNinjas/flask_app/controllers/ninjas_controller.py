from flask import Flask, render_template, request, redirect
from flask_app.models.dojo_model import Dojo             
from flask_app.models.ninja_model import Ninja
from flask_app import app

#table/id/action
@app.route('/ninjas/new')
def new_ninja_form():
    all_dojos = Dojo.get_all()
    return render_template("ninjas_new.html", all_dojos = all_dojos)

@app.route('/ninjas/create', methods = ["POST"])
def create_ninja():
    Ninja.create(request.form)   
    # award_id = Award.create(request.form)    #this is returning award_id
    return redirect(f'/dojos/{request.form["dojo_id"]}/view')
   

