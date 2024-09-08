from app.model import User, db
from flask import render_template, request, redirect, url_for
from app.user import user_blueprint

@user_blueprint.route("/landing", endpoint="land")
def land():
    users = User.query.all()
    return render_template("users/landing.html", users=users)

@user_blueprint.route("/show/<int:id>", endpoint="show_user")
def show(id):
    user = User.query.get(id)  # Changed from users to user to match singular form
    return render_template("users/show.html", user=user)  # Changed variable name to user

@user_blueprint.route("/delete/<int:id>", endpoint="delete_user")
def delete_user(id):
    user = User.query.get(id)  # Changed from users to user to match singular form
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for("user_blueprint.land"))

@user_blueprint.route("/create", endpoint="create_user", methods=['GET', "POST"])
def create():
    if request.method == "POST":
        user = User(
            username=request.form['username'],  
            age=request.form['age'],
            image=request.form['image']
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_blueprint.land"))
    return render_template("users/create.html")

@user_blueprint.route("/edit/<int:id>", endpoint="edit_user", methods=['GET', "POST"])
def edit(id):
    user = User.query.get(id) 
    if request.method == "POST":
        user.username = request.form['username'] 
        user.age = request.form['age']
        user.image = request.form['image']
        db.session.commit()
        return redirect(url_for("user_blueprint.land"))
    return render_template("users/edit.html", user=user)  
