from core.player import Player
from core.enemy import Enemy
from core.combat import CombatSystem
from config.configuration_loader import Config
import json

# Load configuration
with open("config/configuration.json") as f:
    data = json.load(f)

configuration = Config(data)

# Create Objects
player_stats = configuration.player.get_player_stats("warrior") 
enemy_stats = configuration.enemy.get_base_stats()

player = Player(player_stats)
enemy = Enemy(enemy_stats, configuration.ai)

# Combat
combat = CombatSystem()

combat.resolve_attack(player, enemy)
combat.resolve_attack(enemy, player)

combat = CombatSystem()

combat.resolve_attack(player, enemy)
combat.resolve_attack(enemy, player)