import pokemon 
import utilities
import json

class Team:
    
    def __init__(self, data):
        self.pokemons = list()

        entry = {}
        index = 1
        while entry != None: 
            entry = utilities.seek(data, 'pokemon_data', index)
            print "Pokemon"
            print entry
            index = index + 1
            if entry != None:
                self.pokemons.append(pokemon.Pokemon(entry))

    def getDataAsJson(self):
        data = list()
        for entry in self.pokemons:
            data.append(entry.getDataAsJson())
        return data
        
