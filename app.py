import os

from flask import Flask
from flask import render_template
from model.mock_data import Auction


app = Flask(__name__)
auction=Auction()

@app.route('/')
def home():
    return render_template('index.html',timeToBid = auction.timeToBid)

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
