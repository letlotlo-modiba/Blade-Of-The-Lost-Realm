import unittest
from core.enemy import Enemy


class DummyAIConfig:
    def __init__(self, aggression=0.7, reaction_time=0.3):
        self.aggression = aggression
        self.reaction_time = reaction_time

    def get_aggression(self):
        return self.aggression

    def get_reaction_time(self):
        return self.reaction_time


class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.stats = {"health": 80, "damage": 12}
        self.ai = DummyAIConfig(aggression=0.7)
        self.enemy = Enemy(self.stats, self.ai)

    def test_enemy_initialisation(self):
        self.assertEqual(self.enemy.health, 80)
        self.assertEqual(self.enemy.damage, 12)
        self.assertEqual(self.enemy.attack(), 12)

    def test_enemy_decide_action_attack(self):
        self.assertEqual(self.enemy.decide_action(), "attack")

    def test_enemy_decide_action_retreat(self):
        self.enemy.take_damage(60)  # Health 20 < 80 * 0.3 = 24
        self.assertEqual(self.enemy.decide_action(), "retreat")

    def test_enemy_decide_action_wait(self):
        passive_ai = DummyAIConfig(aggression=0.3)
        enemy = Enemy(self.stats, passive_ai)
        self.assertEqual(enemy.decide_action(), "wait")


if __name__ == "__main__":
    unittest.main()
