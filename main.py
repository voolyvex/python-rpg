import json
import random
import sys

#characters = {"Hercules": {"Health": 50, "Attack": {"Sword": 18}}, "Nemean Lion": {"Health": 50, "Attack": {"Claw": 5, "Roar": 9}}, "Cerberus": {"Health": 50, "Attack": {"Bite": 11, "Strength of Hades", 13}}
with open("characters.json") as file:
        character_dict = json.load(file)
defense = 0

def death(monster):
    print("You were killed by " + monster + ".")
    new_game = input("Play again? (y/n): ").strip().lower()
    while new_game not in ["y","n"]:
        new_game = input("Play again? (y/n): ").strip().lower()
    if new_game == "n":
        print("\nGame Over")
        sys.exit()
    else:
        main()

def victory(monster):
    print("Wow, you defeated " + monster + ".")
    user_prompt = input("Continue? (y/n): ").strip().lower()
    while user_prompt not in ["y","n"]:
        user_prompt = input("Continue? (y/n): ").strip().lower()
    if user_prompt == "n":
        print("\nGame Over")
        sys.exit()
    else:
        equip_prompt = input("Equip the Lion Skin? (y/n): ").strip().lower()
        while equip_prompt not in ["y","n"]:
            equip_prompt = input("Equip the Lion Skin? (y/n): ").strip().lower()
            if equip_prompt == "n":
                print("\nYou leave the lion's skin as is and depart.")
            else:
                print("Lion Skin equipped\nDefense +2")
                defense += 2
                       # character_dict["Hercules"]
def boss_fight(boss, hero):        
    print("You are in a boss fight vs", boss)
    print("Type text command:  'Attack' or 'Item'")
    while (character_dict[boss]["Health"] > 0) and (character_dict[hero]["Health"] > 0):
        print(hero, "HP: ", character_dict[hero]["Health"])
        print(boss, "HP: ", character_dict[boss]["Health"])
        action = input("Choose an action: ").strip().lower()
        if action == "attack":
            attack_damage = attack()
            character_dict[boss]["Health"] -= attack_damage
            hero_damaged = random_attack(boss)
            character_dict[hero]["Health"] -= hero_damaged

        elif action == "item":
            item_effect = item()
            character_dict[hero]["Health"] += item_effect
            print(hero, " is healed +25 HP")
            hero_damaged = random_attack(boss)
            character_dict[hero]["Health"] -= hero_damaged
            print(boss, "inflicts", hero_damaged, "damage")

    if (character_dict[boss]["Health"] <= 0):
        victory(boss)
    else:
        death(boss)

def attack():
    attack_prompt = "Attack with Sword or Fist?\n Type text command:  'Sword' or 'Fist'"
    return(10)

def item():
    print("Hercules has: Boar Meat")
    item_prompt = input("Use item? Boar Meat (y/n): ").strip().lower()
    if item_prompt == 'y':
        return(25)
    else:
        return(25)

def random_attack(boss):
    attack_int = random.randrange(0,1)
    if attack_int == 0:
        print(boss, "attacks with", character_dict[boss]["Attack"][0][0])
        damage = character_dict[boss]["Attack"][0][1]
    else:
        print(boss, "attacks with", character_dict[boss]["Attack"][1][0])
        damage = character_dict[boss]["Attack"][1][1]
    return(damage)

def main():
    
    print("""
        \nYou are Hercules, the greatest of the Greek Heroes!
You have been tasked by King Eurystheus to slay the vicious Nemean Lion, defeat the
nine-headed Lernaean Hydra, and capture Cerberus, the guard dog of the underworld.\n
""")
    user_prompt = input("Start Game (y/n): ").strip().lower()
    while user_prompt not in ["y","n"]:
        user_prompt = input("Start Game (y/n): ").strip().lower()
    if user_prompt == "n":
        print("\nGame Over")
    else:
        print("""
        \nYou make the long journey to the Nemean Lion.
The lion laughs and snarls, 'You dare challenge me?'\n
""")
        hero = "Hercules"
        boss_fight("Nemean Lion", hero)



main()