from pathlib import Path
import json
from core.player import Player
from core.enemy import Enemy
from core.combat import CombatSystem
from config.configuration_loader import Config

# Load configuration
config_path = Path(__file__).parent / "config" / "configuration.json"
with open(config_path) as f:
    data = json.load(f)

configuration = Config(data)

# Create Objects
player_stats = configuration.player.get_player_stats("warrior")
enemy_stats = configuration.enemy.get_base_stats()

player = Player(player_stats)
enemy = Enemy(enemy_stats, configuration.ai)

# Combat
combat = CombatSystem(configuration.combat.get_all())

# --- MAIN GAME LOOP ---
while player.is_alive() and enemy.is_alive():

    # Player turn
    print("\n--- Player Turn ---")
    action = input("Choose action (light/heavy/ability/heal): ").strip().lower()

    if action in ["light", "heavy", "ability"]:
        if player.is_on_cooldown(action):
            print(f"{action} is on cooldown!")
        elif action == "ability" and player.mana < 10:
            print("Not enough mana!")
        else:
            combat.resolve_attack(player, enemy, action)

    elif action == "heal":
        player.heal(10)
        print(f"Player heals! Health: {player.health} ")

    else:
        print("Invalid action! Turn skipped.")

    player.reduce_cooldowns()

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

    else:
        print("Enemy waits...")

    if not player.is_alive():
        print("Player defeated!")
        break
