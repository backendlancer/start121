from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'HELLO WORLD!! HEROKU APP IS FINALLY WORKING. BOOYAH'


if __name__ == '__main__':
    app.run()
