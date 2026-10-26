class Entity:
    def __init__(self, health):
        self.max_health = health
        self.health = health
        self.alive = health > 0

    # --- TAKE DAMAGE ---
    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("Damage cannot be negative")

        self.health -= amount
        self.health = max(0, min(self.health, self.max_health))

        if self.health == 0:
            self.alive = False

    def is_alive(self):
        return self.alive
