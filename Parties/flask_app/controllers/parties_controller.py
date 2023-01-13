from flask_app import app
from flask import Flask, render_template, request, redirect, session         
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask_app.models.party_model import Party
from flask import flash


#table/id/action
@app.route('/parties/new')
def new_party_form():
    if "user_id" not in session:
        return redirect('/')
    return render_template("parties_new.html")

@app.route('/parties/create', methods=['post'])
def create_party():
    if "user_id" not in session:
        return redirect('/')
    if not Party.validator(request.form):
        return redirect('/parties/new')
    party_data = {
        **request.form,
        'user_id' : session['user_id']
    }
    Party.create(party_data)
    return redirect('/dashboard')

@app.route('/parties/<int:id>/view')
def get_one_party(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id':id
    }
    one_party = Party.get_one(data)
    return render_template("parties_one.html", one_party=one_party)

@app.route('/parties/<int:id>/edit')
def edit_party_form(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id':id
    }
    one_party = Party.get_one(data)
    return render_template("parties_edit.html", one_party=one_party)

@app.route('/parties/<int:id>/update', methods=['post'])
def update_party(id):
    if "user_id" not in session:
        return redirect('/')
    if not Party.validator(request.form):
        return redirect(f"/parties/{id}/edit")
    update_data = {
        **request.form,
        'id' : id
        }
    # data = {
    #     'id' : id
    # }
    # this_party = Party.get_one(data)                      ####extras
    # if not this_party.user_id == session['user_id']:      ####extras
    #     flash("Not yours, hands off!!")
    #     return redirect("/dashboard")
    Party.update(update_data)
    return redirect('/dashboard')

@app.route('/my_parties')
def show_users_parties():
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    logged_user = User.get_by_id(data)
    return render_template('my_parties.html', logged_user = logged_user)

@app.route('/parties/<int:id>/delete')
def delete_party(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    # this_party = Party.get_one(data)                      ####extras
    # if not this_party.user_id == session['user_id']:      ####extras
    #     flash("Not yours, hands off!!")
    #     return redirect("/dashboard")
    Party.delete(data)
    return redirect('/dashboard')