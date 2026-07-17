from core.entity import Entity

class Enemy(Entity):
    def __init__(self, stats, ai_config):
        super().__init__(stats["health"])

        self.damage = stats.get("damage", 0)
        self.aggression = ai_config.get_aggression()
        self.reaction_time = ai_config.get_reaction_time()

    def attack(self):
        return self.damage

    def decide_action(self):
        if self.health < self.max_health * 0.3:
            return "retreat"
        
        elif self.aggression > 0.5:
            return "attack"
        else:
            return "wait"