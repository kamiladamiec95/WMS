from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/users")
def users():
    return render_template("users.html")
    
@app.route("/nav", methods = ['POST', 'GET'])
def nav():
    if request.method == 'POST':
        # result = request.form
        return render_template("navigationBar.html")

if __name__ == '__main__':
    app.run(debuge=True)    



# @app.route("/hello/")
# def home():
#     test = {'polish': 5, 'english': 10, 'italian': 20}
#     return render_template('hello.html', mark = test)

# if __name__ == '__main__':
#     app.run(debug=True)