from core.entity import Entity

class Player(Entity):
    def __init__(self, stats):
        super().__init__(stats["health"])

        self.max_mana = stats["mana"]
        self.mana = stats["mana"]

        self.strength = stats.get("strength", 0)
        self.intelligence = stats.get("intelligence", 0)
        self.cooldowns = {
            "light_attack": 0,
            "heavy_attack": 0,
            "ability": 0
            }


    # --- HEAL ---
    def heal(self, amount):
        if amount < 0:
            raise ValueError("Heal cannot be negative")
        
        self.health = min(self.max_health, self.health + amount)

    # --- ATTACK ---
    def attack(self):
        return self.strength
    
    # --- ATTACK/ABILITY METHODS ---
    def light_attack(self):
        return int(self.strength * 0.8)

    def heavy_attack(self):
        return int(self.strength * 1.5)

    def use_ability(self):
        if self.mana < 10:
            print("Not enough mana!")
            return 0
        self.mana -= 10
        return int(self.intelligence * 2)


    # --- COOLDOWN HANDLING ---
    def reduce_cooldowns(self):
        for key in self.cooldowns:
            if self.cooldowns [key] > 0:
                self.cooldowns[key] -= 1
    