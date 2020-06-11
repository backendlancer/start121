from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'KEMON ACHO.ETA AMAR FIRST WEBSITE'


if __name__ == '__main__':
    app.run()
