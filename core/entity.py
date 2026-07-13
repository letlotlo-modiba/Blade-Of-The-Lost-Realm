class Entity:
    def __init__(self, health):
        self.max_health = health
        self.health = health
        self.alive = True

    # --- TAKE DAMAGE ---
    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("Damage cannot be negative")
        
        self.health -= amount

        if self.health <= 0:
            self.health = 0
            self.alive = False

    def is_alive(self):
        return self.alive