

class CombatSystem:
    def resolve_attack(self, attacker, defender):
        damage = attacker.attack()
        defender.take_damage(damage)

        print(f"{attacker.__class__.__name__} deals {damage} damage")
        print(f"{defender.__class__.__name__} health: {defender.health}")
