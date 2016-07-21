import urllib2
import json

class Pokemon:

    def __init__(self, data):
        self.id = data["pokemon_id"]
        self.capture_date = data["creation_time_ms"]
        self.sprite = None
        self.retrieveSprite()

    def retrieveSprite(self):
        self.sprite = "http://pokeapi.co/media/img/"+str(self.id)+".png"

    def getDataAsJson(self):
        return vars(self)