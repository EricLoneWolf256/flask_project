from operator import ge

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    first_name = "Westside"
    last_name = "Saint-Ghost"
    course = ["Python",
               "Flask",
               "Django",
               "JavaScript"]
              
    city = "Los Angeles"
    price = 2500
    return render_template('profile.html', first_name=first_name, last_name=last_name,
                           course=course, 
                           city=city,
                            price=price)


if __name__ == '__main__':
    app.run(debug=True)