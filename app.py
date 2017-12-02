from __future__ import print_function
import sys

from flask import Flask, render_template, request
app = Flask(__name__)


types = [
{code: "airport", val: "Airports"},
{code: "amusement_park", val: "Amusement Parks"},
{code: "aquarium", val: "Aquariums"},
{code: "art_gallery", val: "Art Galleries"},
{code: "bakery", val: "Bakeries"},
{code: "bar", val: "Bars"},
{code: "beauty_salon", val: "Beauty Salons"},
{code: "book_store", val: "Book Stores"},
{code: "bowling_alley", val: "Bowling Allies"},
{code: "bus_station", val: "Bus Stations"},
{code: "cafe", val: "Cafes"},
{code: "casino", val: "Casinos"},
{code: "clothing_store", val: "Clothing Stores"},
{code: "florist", val: "Florists"},
{code: "gym", val: "Gyms"},
{code: "hindu_temple", val: "Hindu Temples"},
{code: "hospital", val: "Hospitals"},
{code: "jewelry_store", val: "Jewelry Stores"},
{code: "laundry", val: "Laundries"},
{code: "library", val: "Libraries"},
{code: "liquor_store", val: "Liquor Stores"},
{code: "mosque", val: "Mosques"},
{code: "movie_theater", val: "Movie Theaters"},
{code: "museum", val: "Museums"},
{code: "night_club", val: "Night Clubs"},
{code: "park", val: "Parks"},
{code: "restaurant", val: "Restaurants"},
{code: "school", val: "Schools"},
{code: "shoe_store", val: "Shoe Stores"},
{code: "shopping_mall", val: "Shopping Malls"},
{code: "spa", val: "Spas"},
{code: "stadium", val: "Stadiums"},
{code: "store", val: "Stores"},
{code: "subway_station", val: "Subway Stations"},
{code: "train_station", val: "Train Stations"},
{code: "university", val: "Universities"},
{code: "zoo", val: "Zoos"}
];



@app.route("/")
def init():
    return render_template("main.html", types=types)

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
