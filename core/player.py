from core.entity import Entity

class Player(Entity):
    def __init__(self, stats):
        super().__init__(stats["health"])

        self.max_mana = stats["mana"]
        self.mana = stats["mana"]

        self.strength = stats.get("strength", 0)
        self.intelligence = stats.get("intelligence", 0)


    # --- HEAL ---
    def heal(self, amount):
        if amount < 0:
            raise ValueError("Heal cannot be negative")
        
        self.health = min(self.max_health, self.health + amount)

    # --- ATTACK ---
    def attack(self):
        return self.strength
    