import os

from flask import Flask, request
from flask import render_template
from model import mock_data
from model.mock_data import Auction
app = Flask(__name__)

auction=Auction()

artist = mock_data.getDummyArtist()

@app.route('/')
def home():
    return render_template('index.html',timeToBid = auction.timeToBid,artist = artist)

@app.route('/login',methods=['POST'])
def login():

    for value in request.form:
        print value

    username=request.form['username']
    password=request.form['password']
    return render_template('index.html',timeToBid = auction.timeToBid,artist = artist, username = username)

@app.route("/bid/<value>")
def bid(value):
    auction.addBid(value)

@app.route("/getValue")
def getValue():
    return '<h2>'+str(auction.actualValue)+'$</h2><h4>Precio Actual</h4>'

@app.route("/getMiValue")
def getValue():
    return '<h2>'+str(auction.actualValue)+'$</h2><h4>Nuestro Precio</h4>'

@app.route("/getFuturePrice/<value>")
def getFuturePrice(value):
    index = int(value)
    data = auction.pricesInterval[index-1]
    return str(data)


@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
