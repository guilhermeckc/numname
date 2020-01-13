from flask import Flask
from numbername import number_name

app = Flask(__name__)


@app.route('/')
def homepage():
    return "This application return a integer number name." \
           "You must provide a integer number in range [-99999, 99999] after '/' on url." \
           'Example: http://127.0.0.1:5000/8 will return {8: "oito"}'


@app.route('/<key>')
def get_name(key):
    return number_name(key)


if __name__ == "__main__":
    app.run()
