from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def init():
    return render_template("main.html")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route('/', methods=['POST'])
def submit():


    return render_template("result.html")
