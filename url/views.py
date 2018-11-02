from flask import Flask, redirect, request
from pymongo import MongoClient

#constants
DEFAULT_LENGTH = 7
ALLOWED_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

#globals
client = MongoClient('localhost', 27017)
tinyurl_db = client['tinyurl']
coll = tinyurl_db['urlmaps']
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
	if request.method == "POST":
		long_url = request.form['long_url']
		short_url = request.form['short_url']
		
		#random
		if short_url is None or "":
			rand_url = gen_random_string()
			coll.insert_one({"short_url": rand_url, "long_url": long_url})
			return "success"
		#selected
		else:
			result = coll.find_one({"short_url": short_url})
			if result is None:
				coll.insert_one({"short_url": short_url, "long_url": long_url})
				return "success"
			else:
				return "error template"
	else:
		return "render template"

@app.route('/<short_url>')
def lookup(short_url):
	result = coll.find_one({"short_url": short_url})
	if result is None:
		return "should be an error template"
	else:
		redirect(result['long_url'])

def gen_random_string(len=DEFAULT_LENGTH, allowed_chars=ALLOWED_CHARS):
	rand = ''.join(random.choice(allowed_chars) for i in range(len))
	while(coll.find_one({"short_url": rand}) is not None):
		rand = ''.join(random.choice(allowed_chars) for i in range(len))
	return rand
	
