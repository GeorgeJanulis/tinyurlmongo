from flask import Flask, request, render_template, redirect
import sys
from pymongo import MongoClient
from urllib.request import urlopen
import random

app = Flask(__name__)
client = MongoClient('localhost', 27017)
tinyurl_db = client['tinyurl']
coll = tinyurl_db['urlmaps']

DEFAULT_LENGTH = 7
ALLOWED_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

@app.route('/', methods=["POST", "GET"])
def index():
	if request.method == "POST":
		long_url = validate_url(request.form['long_url'])
		short_url = request.form['short_url']

		if long_url is "":
			return render_template("index.html", error="Invalid long url")
		
		if short_url is None or short_url is "":
			rand_url = gen_random_string()
			coll.insert_one({"short_url": rand_url, "long_url": long_url})
			return render_template("index.html", url=rand_url)
		else:
			result = coll.find_one({"short_url": short_url})

			if result is None:
				coll.insert_one({"short_url": short_url, "long_url": long_url})
				return render_template("index.html", url = short_url)
			else:
				return render_template("index.html", error="Error: short url already exists!")
	else:
		return render_template("index.html", homepage="ERROR")
	


@app.route('/<short_url>')
def lookup(short_url):
	result = coll.find_one({"short_url": short_url})

	if result is None:
		return "error template"
	else:
		return redirect(result["long_url"])
	
def gen_random_string(len=DEFAULT_LENGTH, allowed_chars=ALLOWED_CHARS):
	rand = ''.join(random.choice(allowed_chars) for i in range(len))
	while(coll.find_one({"short_url": rand}) is not None):
		rand = ''.join(random.choice(allowed_chars) for i in range(len))
	return rand

def validate_url(long_url):
		if not long_url.startswith("https://") and not long_url.startswith("http://"):
			long_url = "http://" + long_url
		try: 
			ret = urlopen(long_url)
			if ret.code >= 400:
				long_url = ""
		except:
			long_url = ""
		return long_url