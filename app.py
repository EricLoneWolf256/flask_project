from operator import ge

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    first_name = "Westside"
    last_name = "Saint-Ghost"
    is_logged_in = True
    marks =  88
    courses = ['Python', 'Java', 'C++', 'JavaScript']

    student = { 
        "name": "Westside Saint-Ghost",
        "age": 25,
        "city": "New York",
    }
    return render_template('index.html', first_name=first_name, last_name=last_name,
                           is_logged_in=is_logged_in, marks=marks, courses=courses, student=student)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)