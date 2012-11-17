import os

from flask import Flask
from flask import render_template
import datetime
#from model.mock_data import Auction


app = Flask(__name__)

@app.route('/')
def home():
    #auction=Auction.new

    return render_template('index.html',time = datetime.datetime.now())

@app.route('/hello')
def helloWorld():
    return "Hello world"

@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
