import unittest
import json
from pathlib import Path
from config.configuration_loader import Config


class TestConfigLoader(unittest.TestCase):
    def setUp(self):
        config_path = Path(__file__).parent.parent / "config" / "configuration.json"
        with open(config_path) as f:
            self.data = json.load(f)
        self.config = Config(self.data)

    def test_load_game_config(self):
        self.assertEqual(self.config.game.get_title(), "Blade Of The Lost Realm")
        self.assertEqual(self.config.game.get_version(), "0.1.0")

    def test_load_player_stats(self):
        stats = self.config.player.get_player_stats("warrior")
        self.assertEqual(stats["health"], 120)
        self.assertEqual(stats["strength"], 15)

    def test_load_enemy_stats(self):
        enemy_stats = self.config.enemy.get_base_stats()
        self.assertEqual(enemy_stats["health"], 80)
        self.assertEqual(enemy_stats["damage"], 12)

    def test_load_ai_config(self):
        self.assertEqual(self.config.ai.get_aggression(), 0.7)
        self.assertEqual(self.config.ai.get_reaction_time(), 0.3)
        self.assertEqual(self.config.ai.get_pathfinding(), "A*")

    def test_load_combat_config(self):
        combat = self.config.combat.get_all()
        self.assertIn("crit_chance", combat)
        self.assertIn("dodge_chance", combat)


if __name__ == "__main__":
    unittest.main()
