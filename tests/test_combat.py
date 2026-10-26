import unittest
from unittest.mock import patch
from core.combat import CombatSystem
from core.player import Player
from core.enemy import Enemy
from tests.test_enemy import DummyAIConfig


class TestCombatSystem(unittest.TestCase):
    def setUp(self):
        self.combat_config = {
            "crit_chance": 0.0,
            "crit_multiplier": 1.5,
            "dodge_chance": 0.0,
            "cooldowns": {"light": 0.5, "heavy": 1.5, "ability": 5}
        }
        self.combat = CombatSystem(self.combat_config)
        self.player_stats = {
            "health": 100,
            "mana": 30,
            "strength": 20,
            "intelligence": 25
        }
        self.enemy_stats = {"health": 100, "damage": 10}
        self.player = Player(self.player_stats)
        self.enemy = Enemy(self.enemy_stats, DummyAIConfig())

    def test_resolve_attack_default(self):
        self.combat.resolve_attack(self.enemy, self.player)
        self.assertEqual(self.player.health, 90)

    def test_resolve_attack_light(self):
        self.combat.resolve_attack(self.player, self.enemy, "light")
        # 20 * 0.8 = 16 damage
        self.assertEqual(self.enemy.health, 84)
        self.assertTrue(self.player.is_on_cooldown("light"))

    def test_resolve_attack_heavy(self):
        self.combat.resolve_attack(self.player, self.enemy, "heavy")
        # 20 * 1.5 = 30 damage
        self.assertEqual(self.enemy.health, 70)
        self.assertTrue(self.player.is_on_cooldown("heavy"))

    def test_resolve_attack_ability(self):
        self.combat.resolve_attack(self.player, self.enemy, "ability")
        # 25 * 2 = 50 damage
        self.assertEqual(self.enemy.health, 50)
        self.assertEqual(self.player.mana, 20)
        self.assertTrue(self.player.is_on_cooldown("ability"))

    def test_resolve_attack_ability_no_mana(self):
        self.player.mana = 5
        self.combat.resolve_attack(self.player, self.enemy, "ability")
        # Enemy should not take damage
        self.assertEqual(self.enemy.health, 100)
        self.assertEqual(self.player.mana, 5)

    def test_resolve_attack_critical_hit(self):
        crit_config = dict(self.combat_config, crit_chance=1.0)
        combat = CombatSystem(crit_config)
        combat.resolve_attack(self.enemy, self.player)
        # 10 * 1.5 = 15 damage
        self.assertEqual(self.player.health, 85)

    def test_resolve_attack_dodge(self):
        dodge_config = dict(self.combat_config, dodge_chance=1.0)
        combat = CombatSystem(dodge_config)
        combat.resolve_attack(self.player, self.enemy, "heavy")
        # Enemy dodged, so no damage taken
        self.assertEqual(self.enemy.health, 100)
        # But player still performed action, so heavy goes on cooldown
        self.assertTrue(self.player.is_on_cooldown("heavy"))


if __name__ == "__main__":
    unittest.main()
