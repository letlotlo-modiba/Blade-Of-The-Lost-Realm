import random

class CombatSystem:
    def __init__(self, combat_config):
        self.combat_config = combat_config

    def resolve_attack(self, attacker, defender, action="attack"):
        # --- ACTION LOGIC ---
        if action == "light" and hasattr(attacker, "light_attack"):
            damage = attacker.light_attack()
        elif action == "heavy" and hasattr(attacker, "heavy_attack"):
            damage = attacker.heavy_attack()
        elif action == "ability" and hasattr(attacker, "use_ability"):
            damage = attacker.use_ability()
        else:
            damage = attacker.attack()

        if damage <= 0:
            return

        # --- DODGE ---
        if random.random() < self.combat_config["dodge_chance"]:
            print(f"{defender.__class__.__name__} dodged the attack!")
            return

        # --- CRITICAL HIT ---
        if random.random() < self.combat_config["crit_chance"]:
            damage *= self.combat_config["crit_multiplier"]
            print("Critical hit!")

        damage = int(damage)

        defender.take_damage(damage)

        print(f"{attacker.__class__.__name__} uses {action} -> {damage} damage")
        print(f"{defender.__class__.__name__} health: {defender.health}")
