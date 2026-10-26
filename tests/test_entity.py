import unittest
from core.entity import Entity


class TestEntity(unittest.TestCase):
    def test_entity_initialisation(self):
        entity = Entity(100)
        self.assertEqual(entity.health, 100)
        self.assertEqual(entity.max_health, 100)
        self.assertTrue(entity.is_alive())

    def test_entity_initialisation_zero_health(self):
        entity = Entity(0)
        self.assertFalse(entity.is_alive())

    def test_take_damage(self):
        entity = Entity(100)
        entity.take_damage(30)
        self.assertEqual(entity.health, 70)
        self.assertTrue(entity.is_alive())

    def test_take_fatal_damage(self):
        entity = Entity(100)
        entity.take_damage(120)
        self.assertEqual(entity.health, 0)
        self.assertFalse(entity.is_alive())

    def test_take_negative_damage_raises(self):
        entity = Entity(100)
        with self.assertRaises(ValueError):
            entity.take_damage(-10)


if __name__ == "__main__":
    unittest.main()
