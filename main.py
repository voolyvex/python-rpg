import random
import json

#characters = {"Hercules": {"Health": 50, "Attack": {"Sword": 18}}, "Nemean Lion": {"Health": 50, "Attack": {"Claw": 5, "Roar": 9}}, "Cerberus": {"Health": 50, "Attack": {"Bite": 11, "Strength of Hades", 13}}

def main():
    with open("characters.json") as file:
        character_dict = json.load(file)

    print(character_dict)
    
    print("""
        \nYou are Hercules, the greatest of the Greek Heroes!
You have been tasked by King Eurystheus to slay the vicious Nemean Lion, defeat the
impossible nine-headed Lernaean Hydra, and capture the guard dog of the underworld — Cerberus.\n
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
        boss_fight(characters["Nemean Lion"])
    
def boss_fight(boss):
    print("You are in a boss fight vs", boss)
   



main()