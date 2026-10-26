import unittest
from core.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.stats = {
            "health": 120,
            "mana": 30,
            "strength": 15,
            "intelligence": 20
        }
        self.player = Player(self.stats)

    def test_initial_state(self):
        self.assertEqual(self.player.health, 120)
        self.assertEqual(self.player.max_health, 120)
        self.assertEqual(self.player.mana, 30)
        self.assertEqual(self.player.max_mana, 30)
        self.assertEqual(self.player.strength, 15)
        self.assertEqual(self.player.intelligence, 20)
        self.assertFalse(self.player.is_on_cooldown("light"))
        self.assertFalse(self.player.is_on_cooldown("heavy"))
        self.assertFalse(self.player.is_on_cooldown("ability"))

    def test_heal(self):
        self.player.take_damage(50)
        self.assertEqual(self.player.health, 70)
        self.player.heal(20)
        self.assertEqual(self.player.health, 90)

    def test_heal_does_not_exceed_max_health(self):
        self.player.take_damage(10)
        self.player.heal(50)
        self.assertEqual(self.player.health, 120)

    def test_heal_dead_player_does_nothing(self):
        self.player.take_damage(120)
        self.assertFalse(self.player.is_alive())
        self.player.heal(50)
        self.assertEqual(self.player.health, 0)
        self.assertFalse(self.player.is_alive())

    def test_heal_negative_raises(self):
        with self.assertRaises(ValueError):
            self.player.heal(-5)

    def test_light_attack_and_cooldown(self):
        damage = self.player.light_attack()
        self.assertEqual(damage, int(15 * 0.8))
        self.assertTrue(self.player.is_on_cooldown("light"))

        # Calling again while on cooldown returns 0
        self.assertEqual(self.player.light_attack(), 0)

        # Reducing cooldown restores availability
        self.player.reduce_cooldowns()
        self.assertFalse(self.player.is_on_cooldown("light"))

    def test_heavy_attack_and_cooldown(self):
        damage = self.player.heavy_attack()
        self.assertEqual(damage, int(15 * 1.5))
        self.assertTrue(self.player.is_on_cooldown("heavy"))

        # Heavy attack cooldown is 2
        self.player.reduce_cooldowns()
        self.assertTrue(self.player.is_on_cooldown("heavy"))
        self.player.reduce_cooldowns()
        self.assertFalse(self.player.is_on_cooldown("heavy"))

    def test_use_ability_success(self):
        damage = self.player.use_ability()
        self.assertEqual(damage, int(20 * 2))
        self.assertEqual(self.player.mana, 20)
        self.assertTrue(self.player.is_on_cooldown("ability"))

    def test_use_ability_on_cooldown(self):
        self.player.use_ability()
        # Second attempt should fail
        damage = self.player.use_ability()
        self.assertEqual(damage, 0)
        self.assertEqual(self.player.mana, 20)

    def test_use_ability_insufficient_mana(self):
        self.player.mana = 5
        damage = self.player.use_ability()
        self.assertEqual(damage, 0)
        self.assertEqual(self.player.mana, 5)
        self.assertFalse(self.player.is_on_cooldown("ability"))


if __name__ == "__main__":
    unittest.main()
