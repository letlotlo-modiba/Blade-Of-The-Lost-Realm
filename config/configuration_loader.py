import json
from pathlib import Path


class Config:
    def __init__(self, data):
        self.data = data
        self.player = self.PlayerConfig(data["player"])
        self.display = self.DisplayConfig(data["display"])
        self.game = self.GameConfig(data["game"])
        self.enemy = self.EnemyConfig(data["enemy"])
        self.ai = self.AIConfig(data["ai"])
        self.combat = self.CombatConfig(data["combat"])

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

        def _validate_type(self, key, expected_type):
            value = self._get(key)
            valid_types = (int, float) if expected_type is float else expected_type
            if not isinstance(value, valid_types):
                expected_name = "float or int" if expected_type is float else expected_type.__name__
                raise ValueError(
                    f"Invalid type for '{key}' in {self.section_name}. "
                    f"Expected {expected_name}, got {type(value).__name__}"
                )

    class PlayerConfig(BaseConfig):
        def __init__(self, data):
            super().__init__(data, "Player")
            self._validate_required(["classes"])

        def get_player_stats(self, class_name):
            classes = self._get("classes")

            if class_name not in classes:
                raise ValueError(f"Class '{class_name}' not found in Player configuration")

            if "stats" not in classes[class_name]:
                raise ValueError(f"Missing 'stats' for class '{class_name}'")

            return classes[class_name]["stats"]

    class DisplayConfig(BaseConfig):
        def __init__(self, data):
            super().__init__(data, "Display")
            self._validate_required(["resolution"])

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

            self._validate_type("aggression", float)
            self._validate_type("reaction_time", float)
            self._validate_type("pathfinding", str)

        def get_aggression(self):
            return self._get("aggression")

        def get_reaction_time(self):
            return self._get("reaction_time")

        def get_pathfinding(self):
            return self._get("pathfinding")

    class CombatConfig(BaseConfig):
        def __init__(self, data):
            super().__init__(data, "Combat")
            self._validate_required(["crit_chance", "crit_multiplier", "dodge_chance"])

        def get_all(self):
            return self.data


if __name__ == "__main__":
    config_file = Path(__file__).parent / "configuration.json"
    with open(config_file) as f:
        data = json.load(f)

    configuration = Config(data)
