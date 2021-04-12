from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello dunia"

@app.route("/profil")
def profil():
    return "Ini Adalah profil"


if __name__ == "__main__":
    app.run() 