import random

class CombatSystem:
    def __init__(self, combat_config):
        self.combat_config = combat_config

    def resolve_attack(self, attacker, defender):
        damage = attacker.attack()

        # --- DODGE ---
        if random.random() < self.combat_config["dodge_chance"]:
            print(f"{defender.__class__.__name__} dodged the attack!")
            return
        
        damage = attacker.attack()
        
        # --- CRITICAL HIT ---
        if random.random() < self.combat_config["crit_chance"]:
            damage *= self.combat_config["crit_multiplier"]
            print("Critical hit!")

        damage = int(damage)

        defender.take_damage(damage)

        print(f"{attacker.__class__.__name__} deals {damage} damage")
        print(f"{defender.__class__.__name__} health: {defender.health}")