import threading
import time

__author__ = 'yamit'

class Auction(threading.Thread):

    timeToBid = (60*60*24)-5
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

