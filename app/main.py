from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlite3
from faker import Faker
from flask_sqlalchemy import SQLAlchemy

# from flask_login import UserMixin, login_user, loginManager, login_required, logout_user, current_user

app = Flask(__name__)

app_ctx = app.app_context()
app_ctx.push()

app.config['SECRET_KEY'] = 'secret'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users2.db'

db = SQLAlchemy(app)

class Users(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name

class WarehouseReleases(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name

class Products(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name


class Przyjecia(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name           


class LoginForm(FlaskForm):
    login = StringField("Login")
    password = StringField("Password")
    submit = SubmitField("Submit")

class AddUser(FlaskForm):
    login = StringField("Login")
    password = StringField("Password")
    name = StringField("Name") 
    submit = SubmitField("Add")   

db.create_all()

users = []

# user = Users(name="test", email="test2@test.pl")
# db.session.add(user)
# db.session.commit()

faker = Faker()

user = Users(name=faker.name(),
            email=faker.email())
db.session.add(user)
users.append(user.name)
db.session.commit()

user = Users(name=faker.name(),
            email=faker.email())
db.session.add(user)
users.append(user.name)

db.session.commit()

result = user.query.all()
for i in result:
    print(i.__dict__)

# @login.required
@app.route("/", methods=['GET', 'POST'])
def home():
    # login = 'test'
    form = LoginForm()#request.form)
    # print(form.validate_on_submit())
    print(form.validate_on_submit())
    # if request.method == 'POST':
    if form.validate_on_submit():
        print('test123')
        login = form.login.data 
        # if login == 'test':
        return redirect(url_for("nav"))
    print(form.errors)        
    return render_template("home2.html", form=form)


@app.route("/add_user", methods=['GET', 'POST'])
def add_user():
    # login = 'test'
    form = AddUser()#request.form)
    # print(form.validate_on_submit())
    
    if form.validate_on_submit():
        print('test123')
        login = form.login.data 
        # if login == 'test':
        flash('User added successfully')
        flash('User added successfully2')
    print(form.errors)        
    return render_template("add_user.html", form=form)    

# @app.route("/users")
# def users(items):
#     return render_template("users.html", items = itemsU)
    
@app.route("/nav", methods = ['POST', 'GET'])
def nav():
    # if request.method == 'POST':
        # result = request.form["nm"]
    return render_template("navigationBar.html")


@app.route("/users")
def users():
    form = AddUser()
    result = list(user.query.all())
    users = ['Adam', 'Kamil']
    return render_template("users.html", users= result,form=form)


@app.route("/test")
def test():
    return render_template("test.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500    

if __name__ == '__main__':
    app.run(debuge=True)

    