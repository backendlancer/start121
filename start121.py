from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "LET'S CHANGE THE LINES. BUT YOU CAN'T UNDERSTAND"


if __name__ == '__main__':
    app.run()
