import json


class Config:
    def __init__(self, data):
        self.data = data
        self.player = self.PlayerConfig(data["player"])
        self.display = self.DisplayConfig(data["display"])
        self.game = self.GameConfig(data["game"])
        self.enemy = self.EnemyConfig(data["enemy"])
        self.ai = self.AIConfig(data["ai"])

    class BaseConfig:
        def __init__(self, data, section_name):
            self.data = data
            self.section_name = section_name

        def _get(self, key):
            if key not in self.data:
                raise ValueError(f"Missing '{key}' in {self.section_name} configuration")
            return self.data[key]
        
        def _validate_required(self, required_keys):
            for key in required_keys:
                if key not in self.data:
                    raise ValueError(f"Missing '{key}' in {self.section_name} configuration")


    class PlayerConfig(BaseConfig):
        def __init__(self, data):
            super().__init__(data, "Player")
            self._validate_required(["classes"])

        def  get_player_stats(self, class_name):
            classes = self._get("classes")

            if "stats" not in classes[class_name]:
                raise ValueError(f"Missing 'stats' for class '{class_name}'")

            return classes[class_name]["stats"]

    class DisplayConfig(BaseConfig):
        def __init__(self, data):
            super().__init__(data, "Display")

        def get_resolution(self):
            return self._get("resolution")
          
    class GameConfig(BaseConfig):
        def __init__(self, data):
            super().__init__(data, "Game")
            self._validate_required(["title", "version"])

        def get_title(self):
            return self._get("title")

        def get_version(self):
            return self._get("version")
        
    class EnemyConfig(BaseConfig):
        def __init__(self, data):
            super().__init__(data, "Enemy")
            self._validate_required(["base_health", "base_damage"])

        def get_base_stats(self):
            return {
                "health": self._get("base_health"),
                "damage": self._get("base_damage")
            }
          
    class AIConfig(BaseConfig):
        def __init__(self, data):
            super().__init__(data, "AI")
            self._validate_required(["aggression", "reaction_time", "pathfinding"])
        
        def get_aggression(self):
            return self._get("aggression")
        
        def get_reaction_time(self):
            return self._get("reaction_time")
        
        def get_pathfinding(self):
            return self._get("pathfinding")


with open("configuration.json") as f:
            data = json.load(f)
        
configuration = Config(data)

# Testing output
# print(configuration.game.get_game_title_and_version())
# print(configuration.display.get_resolution())
# print(configuration.player.get_player_stats("warrior"))
# print(configuration.player.get_player_stats("mage"))
# print(configuration.ai.get_aggression())
# print(configuration.ai.get_reaction_time())
# print(configuration.ai.get_pathfinding())
