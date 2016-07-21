import utilities
import team
import json

class Player:

    def __init__(self, data):
        self.username = data["player_data"]["username"]
        self.current_badge = data["player_data"]["equipped_badge"]
        self.since = data["player_data"]["creation_timestamp_ms"]
        #traitement de la monnaie
        self.pokecoin = 0
        self.stardust = 0
        if data["player_data"]["currencies"][0]["name"] == "POKECOIN" and "amount" in data["player_data"]["currencies"][0]:
            self.pokecoin = data["player_data"]["currencies"][0]["amount"]
            if "amount" in data["player_data"]["currencies"][1]:
                self.stardust = data["player_data"]["currencies"][1]["amount"]
        elif data["player_data"]["currencies"][0]["name"] == "STARDUST" and "amount" in data["player_data"]["currencies"][0]:
            self.stardust = data["player_data"]["currencies"][0]["amount"]
            if "amount" in data["player_data"]["currencies"][1]:
                self.pokecoin = data["player_data"]["currencies"][1]["amount"]
            
        self.level = 0
        self.xp = 0
        self.next_xp = 0
        self.captured = 0
        self.encountered = 0
        self.pokedex = 0

        self.team = None

    def setPlayerStats(self, data):
        data = utilities.seek(data, 'player_stats')
        self.level = data['level']
        self.xp = data["experience"]
        self.next_xp = data['next_level_xp']
        self.captured = data["pokemons_captured"]
        self.encountered = data["pokemons_encountered"]
        self.pokedex = data["unique_pokedex_entries"]

    def setTeam(self, data):
        self.team = team.Team(data)

    def getDataAsJson(self):
        data = vars(self)
        data["team"] = self.team.getDataAsJson()

        return data
        