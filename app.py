from flask import Flask

from develop_configure import WELCOME_TEXT

app = Flask(__name__)

@app.route('/')
def index():
    return WELCOME_TEXT

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)