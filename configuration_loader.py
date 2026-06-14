import json


class Config:
    def __init__(self, data):
        self.data = data
        self.player = self.PlayerConfig(data["player"])
        self.display = self.DisplayConfig(data["display"])
        self.game = self.GameConfig(data["game"])
        self.enemy = self.EnemyConfig(data["enemy"])
        self.ai = self.AIConfig(data["ai"])

    class PlayerConfig:
        def __init__(self, data):
            self.data = data

        def  get_player_stats(self, class_name):
            try:
                return self.data["classes"][class_name]["stats"]
            except KeyError:
                raise ValueError(f"Class {class_name} does not exist in configuration")

    class DisplayConfig:
        def __init__(self, data):
            self.data = data

        def get_resolution(self):
            return self.data["resolution"]
          
    class GameConfig:
        def __init__(self, data):
            self.data = data
             
        def get_game_title_and_version(self):
            return self.data["title"]

        def get_version(self):
            return self.data["version"]
        
    class EnemyConfig:
        def __init__(self, data):
            self.data = data
              
        def get_base_stats(self):
            return {
                "health": self.data["base_health"],
                "damage": self.data["base_damage"]
            }
          
    class AIConfig:
        def __init__(self, data):
            self.data = data
        
        def get_aggression(self):
            return self.data["aggression"]
        
        def get_reaction_time(self):
            return self.data["reaction_time"]
        
        def get_pathfinding(self):
            return self.data["pathfinding"]


with open("configuration.json") as f:
            data = json.load(f)
        
configuration = Config(data)

# Testing output
# print(configuration.game.get_game_title_and_version())
# print(configuration.display.get_resolution())
# print(configuration.player.get_player_stats("warrior"))
# print(configuration.player.get_player_stats("mage"))
print(configuration.ai.get_aggression())

