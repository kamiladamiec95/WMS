from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlite3
# from flask_login import UserMixin, login_user, loginManager, login_required, logout_user, current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""
            CREATE TABLE users 
            (
                login text,
                password text

            )
        """)

c.execute("INSERT INTO users VALUES('admin@admin.pl', 'admin')")
c.execute('SELECT * FROM users')
itemsU = dict(c.fetchall())

# print(dict(items))

conn.commit()
conn.close()

class LoginForm(Form):
    login = StringField("Login")
    password = StringField("Password")
    submit = SubmitField("Submit")

@app.route("/", methods=['GET', 'POST'])
def home():
    # login = 'test'
    form = LoginForm(request.form)#request.form)
    # print(form.validate_on_submit())
    
    if request.method == "POST" and form.validate():
        print('test123')
        login = form.login.data 
        # if login == 'test':
        return redirect(url_for("nav"))
    print(form.errors)        
    return render_template("home3.html", form=form)

# @app.route("/users")
# def users(items):
#     return render_template("users.html", items = itemsU)
    
@app.route("/nav", methods = ['POST', 'GET'])
def nav():
    # if request.method == 'POST':
        # result = request.form["nm"]
    return render_template("navigationBar.html")

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("500.html"), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template("500.html"), 500    

if __name__ == '__main__':
    app.run(debuge=True)

    