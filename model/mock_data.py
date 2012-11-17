__author__ = 'yamit'

class Auction():

    time = 60*60*24
    actualValue=500000

    def getStringDate(self):
        oneHour=60*60

        hours=self.time/oneHour
        secs=self.time%oneHour

