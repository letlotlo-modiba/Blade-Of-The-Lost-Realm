from core.entity import Entity

class Player(Entity):
    def __init__(self, stats):
        super().__init__(stats["health"])

        self.max_mana = stats.get("mana", 0)
        self.mana = self.max_mana

        self.strength = stats.get("strength", 0)
        self.intelligence = stats.get("intelligence", 0)
        self.cooldowns = {
            "light": 0,
            "heavy": 0,
            "ability": 0
        }

    # --- HEAL ---
    def heal(self, amount):
        if amount < 0:
            raise ValueError("Heal cannot be negative")
        if not self.alive:
            return

        self.health = min(self.max_health, self.health + amount)

    # --- COOLDOWN HANDLING ---
    def reduce_cooldowns(self):
        for key in self.cooldowns:
            if self.cooldowns[key] > 0:
                self.cooldowns[key] -= 1

    def is_on_cooldown(self, action):
        return self.cooldowns.get(action, 0) > 0

    # --- ATTACK ---
    def attack(self):
        return self.strength

    # --- ATTACK/ABILITY METHODS ---
    def light_attack(self):
        if self.is_on_cooldown("light"):
            print("Light attack is on cooldown!")
            return 0

        self.cooldowns["light"] = 1
        return int(self.strength * 0.8)

    def heavy_attack(self):
        if self.is_on_cooldown("heavy"):
            print("Heavy attack is on cooldown!")
            return 0

        self.cooldowns["heavy"] = 2
        return int(self.strength * 1.5)

    def use_ability(self):
        if self.is_on_cooldown("ability"):
            print("Ability is on cooldown!")
            return 0

        if self.mana < 10:
            print("Not enough mana!")
            return 0

        self.mana -= 10
        self.cooldowns["ability"] = 3
        return int(self.intelligence * 2)
