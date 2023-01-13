from flask_app import app
from flask import Flask, render_template, request, redirect, session         
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe

#table/id/action
@app.route('/recipes/new')
def new_recipe_form():
    if "user_id" not in session:
        return redirect('/')
    return render_template("recipes_new.html")

@app.route('/recipes/create' , methods = ['post'])
def create_recipe():
    if "user_id" not in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect('/recipes/new')
    recipe_data = {
        **request.form,
        'user_id': session['user_id']
    }
    Recipe.create(recipe_data)
    return redirect ('/dashboard')

@app.route('/recipes/<int:id>/view')
def get_one_recipe(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id':id
    }
    one_recipe = Recipe.get_one(data)
    logged_user = User.get_by_id({                #####
        "id" : session['user_id']
    })
    return render_template("recipes_one.html", one_recipe = one_recipe, logged_user = logged_user)

@app.route('/recipes/<int:id>/edit')
def edit_recipe_form(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id':id
    }
    one_recipe = Recipe.get_one(data)
    return render_template("recipes_edit.html",one_recipe = one_recipe)

@app.route('/recipes/<int:id>/update', methods = ['post'])
def update_recipe(id):
    if "user_id" not in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect(f"/recipes/{id}/edit")
    update_data = {
        **request.form,
        'id' : id
    }
    Recipe.update(update_data)
    return redirect('/dashboard')

@app.route('/my_recipes')
def show_users_recipes():
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(data)
    return render_template('my_recipes.html', logged_user = logged_user)

@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id' : id
    }
    Recipe.delete(data)
    return redirect('/dashboard')


