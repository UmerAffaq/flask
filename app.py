from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<string:name>")
def helo(name):
    name = name
    return f"""Hello """
@app.route("/click")
def click():
    return render_template("first.html")
 