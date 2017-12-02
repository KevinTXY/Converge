from __future__ import print_function
import sys

from flask import Flask, render_template, request
app = Flask(__name__)




@app.route("/")
def init():
    return render_template("main.html")

@app.route("/result", methods=['POST'])
def result():

	if request.method == 'POST':

		total = int(request.form.get('total'));
		items = [];

		for i in range(int(total)):
			items.append(request.form.get('item_' + str(i)))

		return render_template("result.html", total = total, items = items)

@app.route('/', methods=['POST'])
def submit():


    return render_template("result.html")
