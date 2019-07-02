import datetime

class History(object):
    def __init__(self, url, film, date = datetime.datetime.now()):
       self.url = url
       self.film = film
       self.date = date

    def __repr__(self):
        return 'In {0}, title: {1} on {2}'.format(self.url, self.film, self.date)