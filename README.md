# TinyURL Service implemented using Flask and MongoDB

## Setup

### Note: These instructions assume that you are using a Mac/Linux machine. If you are running Windows, some of the commands may be different and require that you look up the corresponding Windows command prompt command (i.e. 'how to run flask app windows).

0. Get a copy of this repository by running `git clone https://github.com/mtandrei/tinyurlmongo`
1. Make sure python3, pip3, and virtualenv are installed.
2. Create a virtual environment by running virtualenv venv. This allows us to manage and separate build environments between projects on the same machine with ease.
3. Activate the virtual environment by running `source venv/bin/activate`. You can deactivate it at any time by running `deactivate`
4. Install all of the libraries needed by the project by running `pip3 install -r pip.req`
5. Start up a MongoDB instance by running `mongod` in a separate terminal window. If MongoDB is not installed on your machine, check the MongoDB Docs for relevant instructions: https://docs.mongodb.com/manual/installation/
6. To run the web application run `export FLASK_APP=views` followed by `flask run`. While the former command lets flask know the filename in which the web application exists, the latter simply runs it. You should be able to access the webapp at http://127.0.0.1:5000.


## Overview
If you want to take a crack at building this yourself, simply clone this repositroy, delete views.py, go through every step of setup except 6. and then create a new views.py. Use the views.py in this repository as a reference for the necessary imports. Roughly speaking, you want to develop this app as follows:

1. First, define the routes that will be used in this application. There should be two: one for the home page and one that is responsible for redirecting short urls to the long urls which they are tied to.
2. Think of what should happen at each route in terms of HTTP GET and POST requests: for the home page route I can simply lookup the home page or submit a long and short url pair while the redirecting route should simply redirect the user as specified in step one. Remember, you'll want to store any url pairs in the database so you can look them up later.
3. Now that the basic behavior is implemented, consider edge cases: How can I guarantee that short urls are unique? What should I do if someone tries to use a short url that doesn't exist? There are more than these 2, but this should be enough to get you started.


If you have any questions about the instructions, feel free to shoot me a message.
