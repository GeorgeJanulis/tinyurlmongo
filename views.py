from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(_name_)
client = MongoClient('localhost', 27017)
tinyurl_db = client['tinyurl']
coll = tinyurl_db['urlmaps']

@app.route('/', methods=["POST", "GET"])

def index():
	if request.method == "POST":
		long_url = request.form['long_url']
		short_url = request.form['short_url']

		coll.insert_one({"short_url": short_url, "long_url": "https://" + long_url})
		return render_template("index.html", url=short_url)

	else:
		return render_template("index.html")

@app.route('/<short_url>')
def lookup(short_url):
	result = coll.find_one({"short_url": short_url})
	if result is None:
		return render_template("error.html")

	else:
		return redirect(result["long_url"])
