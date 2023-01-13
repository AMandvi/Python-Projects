from flask import Flask, render_template, request, redirect
from flask_app.models.user_model import User            
from flask_app import app

#full crud routing
#/table_name/id/action
@app.route("/users")
def index():
    all_users = User.get_all()   #method
    return render_template("index.html", all_users = all_users)

@app.route('/users/<int:id>/view')    
def get_one_route(id):
    data = {                          #or this way#
        'id':id
    }
    one_user = User.get_one(data)
    return render_template("users_one.html",one_user = one_user)

@app.route("/users/new")    
def new_user_form():
    return render_template("users_new.html")

@app.route("/users/create", methods = ["POST"])    
def create_user():
    User.create(request.form)
    return redirect("/users")

@app.route("/users/<int:id>/edit")    
def edit_user(id):
    this_user = User.get_one({'id':id})      #can make like this#
    return render_template("users_edit.html", this_user= this_user)

@app.route('/users/<int:id>/update',methods = ['POST'])
def update_user(id):

    #unpacking
    data = {
        'id':id,
        **request.form
    }
    User.update(data)    
    return redirect('/users')

@app.route('/users/<int:id>/delete')  
def delete_user(id):
    User.delete({'id':id})
    return redirect('/users')