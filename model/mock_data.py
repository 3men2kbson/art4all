import threading
import time
from model.artist import Artist

__author__ = 'yamit'

class Auction(threading.Thread):

    timeToBid = (60*60*24)
    actualValue=500000
    canBid=True

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        while self.canBid:
            self.timeToBid = self.timeToBid -1
            if(self.timeToBid == 0):
                self.canBid=False
            time.sleep(1)

def getDummyArtist():
    artist = Artist()
    artist.name='Juan Calzadilla'
    artist.pictureUrl='../static/img/artist.jpg'
    #artist.pictureUrl='http://www.laparaulatailustrada.com/wp-content/uploads/2010/10/juancalzadilla_jpg.jpg'
    artist.description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam dui erat, auctor in viverra at, pharetra eu ligula. Nullam interdum, quam vel malesuada congue, tellus est adipiscing neque, id consequat enim augue sed orci. Fusce sit amet augue sit amet leo convallis dignissim ut sed mi. Nunc aliquet sodales velit vel aliquet. Curabitur id massa ac erat feugiat porttitor. Vestibulum et orci aliquam.'
    return artist