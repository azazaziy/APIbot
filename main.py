from flask import Flask
from flask_sslify import SSLify

#СОЗДАНИЕ СЕРВЕРА
app = Flask(__name__)
sslify = SSLify(app)

@app.route('/')
def index(username):
    return "Hello, %s!" % username

if __name__ == "__main__":
    app.run()