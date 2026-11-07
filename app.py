from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Home Page</h1>"

@app.route('/user/<int:id>')
def user_profile(id):
    return   f"Welcome to the User Profile Page! Used ID:  {id}" 

@app.route ('/price/<float:amount>')
def price(amount):
    return f"The price is: ${amount: }"

@app.route('/student/<uuid:username_id>/<course>')
def student_profile(username_id, course):
    return f"Hello, {username_id}! You are enrolled in the {course} course."

@app.route('/search')

def search():
    name = request.args.get('name', "Guest")
    course = request.args.get('course', "Unknown")
    return f"Hello, {name}! You are searching for the {course} course."


if __name__ == '__main__':
    app.run(debug=True)