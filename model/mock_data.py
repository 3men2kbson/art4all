import threading
import time
from model.artist import Artist

__author__ = 'yamit'

class Auction(threading.Thread):

    timeToBid = (60*60*24)
    #timeToBid = (20)
    actualValue=200000
    canBid=True
    pricesList = [10000,20000,30000,40000,50000,60000]
    pricesInterval = [0,0,0,0,0,0]
    priceNow = 1000000

    def __init__(self):
        self.getPriceInterval()
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        while self.canBid:
            self.timeToBid = self.timeToBid -1
            if(self.timeToBid == 0):
                self.canBid=False
            time.sleep(1)

    def addBid(self,value):
        self.actualValue += int(value)
        #update
        self.getPriceInterval()

    def getPriceInterval(self):

        i=0
        for price in self.pricesList:
            newValue = self.actualValue+price
            self.pricesInterval[i]=newValue
            i+=1
        return self.pricesInterval

def getDummyArtist():
    artist = Artist()
    artist.name='MANUEL CALDERON'
    artist.pictureUrl='../static/img/artist.jpg'
    #artist.pictureUrl='http://www.laparaulatailustrada.com/wp-content/uploads/2010/10/juancalzadilla_jpg.jpg'
    artist.description=''
    return artist