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
combat = CombatSystem(configuration.combat.get_all())

combat.resolve_attack(player, enemy)
combat.resolve_attack(enemy, player)

combat.resolve_attack(player, enemy)
combat.resolve_attack(enemy, player)

# Main game loop
while player.is_alive() and enemy.is_alive():
    # Player turn
    print("\n--- Player Turn ---")
    action = input("Choose action (light/heavy/ability):)".lower()) # player input

    if action == "attack":
        combat.resolve_attack(player, enemy, action)
        player.reduce_cooldowns()
    
    elif action == "heal":
        player.heal(10)
        print(f"Player heals! Health: {player.health} ")
    
    else:
        print("Invalid action! Turn skipped.")

    if not enemy.is_alive():
        print("Enemy defeated!")
        break

    # Enemy turn
    print("\n--- Enemy Turn ---")
    action = enemy.decide_action()

    print(f"Enemy chooses to {action}")
    if action == "attack":
        combat.resolve_attack(enemy, player)

    elif action == "retreat":
        print("Enemy retreats")
        break

    elif action == "wait":
        print("Enemy hesitates...")
        break
    else:
        print("Enemy waits...")

    if not player.is_alive():
        print("Player defeated!")
        break