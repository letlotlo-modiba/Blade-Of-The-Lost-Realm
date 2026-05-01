import json


class Config:
    def __init__(self, data):
        self.data = data

    def get_player_stats(self, class_name):
        try:
            return self.data["player"]["classes"][class_name]["stats"]
        except KeyError:
              raise ValueError(f"Class {class_name} does not exist in configuration")

    def get_resolution(self):
        return self.data["display"]["resolution"]
          
    def get_game_title(self):
        return self.data["game"]["title"]
        
    def get_enemy_base_stats(self):
        return {
             "health": self.data["enemy"]["base_health"],
             "damage": self.data["enemy"]["base_damage"]
        }
          
with open("configuration.json") as f:
            data = json.load(f)
        
configuration = Config(data)

# Testing output
print(configuration.get_game_title())
print(configuration.get_resolution())
print(configuration.get_player_stats("mage"))
print(configuration.get_enemy_base_stats())


        


