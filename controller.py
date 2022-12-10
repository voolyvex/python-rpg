from view import *
from PyQt5.QtWidgets import *
import random
import json

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, **kwargs):
        super(Controller, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.story_text("Press START to play")
        self.fight_text("\t    Welcome to HERAKLES Adventure!\n'Ut aliquam purus sit amet luctus venenatis lectus. Velit euismod in pellentesque massa placerat duis ultricies lacus sed.Ut aliquam purus sit amet luctus venenatis lectus. Velit euismod in pellentesque massa placerat duis ultricies lacus sed.'")
        self.setWindowTitle("HERAKLES")
        self.Title_2.setText("Adventure")
        self.Title_1.setText("HERAKLES")
        self.boss_health_label.setText("Boss HP")
        self.hero_health_label.setText("Hero HP")
        self.itemButton.setToolTip("Use Item: Boar Meat")
        self.itemButton.setText("Item")
        self.attackButton.setToolTip("Execute a random attack")
        self.attackButton.setText("Attack")
        self.startButton.setText("START")
        self.set_image_left("img/landscape_greece_parthenon.jpg")
        self.set_image_right("img/hero_lion_skin_stylized.jpg")
        self.hero = "Herakles"
        try:  # load character stats from json
            with open("characters.json") as file:
                self.character_dict = json.load(file)
        except FileNotFoundError as e:
            print(f"Exception: {e}")
                
        self.startButton.clicked.connect(lambda: self.run())

    def run(self):
        self.set_image_right("img/hero_centaur.jpg")
        self.set_image_left("img/greece_ruins.jpg")
        self.hero_LCD.setProperty("intValue", 000)
        self.boss_LCD.setProperty("intValue", 000)
        self.story_text("You are Herakles of ancient legend.\nYou have been tasked by King Eurystheus to slay the\nvicious Nemean Lion, defeat the nine-headed Lernaean\nHydra, and capture Cerberus--the guard dog of the underworld.")
        self.fight_text("Click CONTINUE ---->")
        self.startButton.setText("CONTINUE")
        self.startButton.clicked.connect(self.main_narrative1)
        
    def main_narrative1(self):
        self.set_image_left("img/nemean-lion-ryan-barger.jpg")
        self.set_image_right("img/hero_lion_hugs.jpg")
        self.story_text("You make the long & humbling journey to Nemea.\nThe Nemean Lion snarls, 'Dare thee challenge?!'")
        self.fight_text("You are in a boss fight vs Nemean Lion")
        self.boss = "Nemean Lion"
        hero_health = int(self.character_dict[self.hero]["Health"])
        boss_health = int(self.character_dict[self.boss]["Health"])
        self.hero_LCD.setProperty("intValue", hero_health)
        self.boss_LCD.setProperty("intValue", boss_health)
        self.startButton.clicked.connect(self.main_narrative2)    
    def main_narrative2(self):
        self.set_image_left("img/hydra.jpg")
        self.set_image_right("img/hero_hydra_with_lion_skin.jpg")
        self.story_text("You travel to the outskirts of Lerna and find the\nadorable lair of the Laernean Hydra.\nOne of the nine heads hisses, 'Dieeee.'")
        self.fight_text("You are in a boss fight vs Laernean Hydra")
        self.boss = "Lernaean Hydra"
        hero_health = int(self.character_dict[self.hero]["Health"])
        boss_health = int(self.character_dict[self.boss]["Health"])
        self.hero_LCD.setProperty("intValue", hero_health)
        self.boss_LCD.setProperty("intValue", boss_health)
        self.startButton.clicked.connect(self.main_narrative3)
    def main_narrative3(self):
        self.set_image_left("img/cerberus_by_moonxels.jpg")
        self.set_image_right("img/femme_hercules.jpg")
        self.story_text("Finally, the entrance to Hell. Oh wow look it's Cerberus. Nice doggy.\n\tNiiiiice doggy.")
        self.fight_text("You are in a boss fight vs Cerberus")
        self.boss = "Cerberus"
        hero_health = int(self.character_dict[self.hero]["Health"])
        boss_health = int(self.character_dict[self.boss]["Health"])
        self.hero_LCD.setProperty("intValue", hero_health)
        self.boss_LCD.setProperty("intValue", boss_health)
        self.startButton.clicked.connect(self.ending)
    def ending(self):
        self.set_image_left("img/ruins_art_armand-bovoso.jpg")
        self.set_image_right("img/hero_lion.jpg")
        self.story_text("GAME OVER")
        self.fight_text("Congratulations! You captured Cerberus.\nKing Eurystheus is actually terrified of Cerberus,\nso you release him back to Hades.")
        self.startButton.setText("THE END")
"""
    Developer note: The following game logic to be integrated with gui interface in 2023.
"""    

    # def death(self, monster):
    #     self.fight_text("You were killed by " + monster + ".")
    #     self.fight_text("\nGame Over\n")
    #     self.fight_text("Click START/CONTINUE to play again.")
    #     self.startButton.clicked.connect(lambda: self.run())

    # def victory(self, monster):
    #     defense = self.character_dict[self.hero]["Defense"]
    #     if monster != "Cerberus":
    #         self.fight_text("Wow, you defeated " + monster + ".")
    #         user_prompt = input("Continue? (y/n): ").strip().lower()
    #         while user_prompt not in ["y","n"]:
    #             user_prompt = input("Continue? (y/n): ").strip().lower()
    #         if user_prompt == "n":
                
    #             self.fight_text("\nGame Over")
                
    #         elif monster == "Nemean Lion":
    #             equip_prompt = input("Equip the Lion Skin? (y/n): ").strip().lower()
    #             while equip_prompt not in ["y","n"]:
    #                 equip_prompt = input("Equip the Lion Skin? (y/n): ").strip().lower()
                
    #             if equip_prompt == "n":
    #                 self.fight_text("\nYou think, 'Why wear clothing, I'm Herakles?!'")
                    
    #                 self.fight_text("You leave the lion's skin as is and depart.")
                    
    #             elif equip_prompt == "y":
    #                 self.character_dict[self.hero]["Defense"] = 2
    #                 self.fight_text("Lion Skin equipped\nDefense +2")
                    
    #         elif monster == "Lernaean Hydra":
                
    #             self.fight_text("You severed the immortal head.")
                
    #             equip_prompt = input("Dip arrows in poison? (y/n): ").strip().lower()
    #             while equip_prompt not in ["y","n"]:
    #                 equip_prompt = input("Dip arrows in poison? (y/n): ").strip().lower()
    #             if equip_prompt == "n":
    #                 self.fight_text("\nYou decide that 'hard mode' is more fun and continue with non-poison arrows.")
    #             elif equip_prompt == "y":
    #                 self.fight_text("Poison Arrows equipped\nAttack Power +6")
    #                 self.character_dict[self.hero]["Attack"][0] = ["Poison Arrows", 15]
    #     else:
            
    #         self.fight_text("Congratulations! You captured Cerberus.\nKing Eurystheus is actually terrified of Cerberus,\nso you release him back to Hades.")
            
    #         self.fight_text("You won the game.")
    #         if defense == 0:
                
    #             self.fight_text("'Skinless' bonus acheived!")
    #         if self.character_dict[self.hero]["Attack"][0][0] != "Poison Arrows":
                
    #             self.fight_text("'Poisonless' bonus acheived!")
            
    #         self.fight_text("Game by voolyvex") 

    # def both_die(self, monster):
        
    #     self.fight_text("\nWow you defeated " + monster + ",")
        
    #     self.fight_text("but you also died in the process :(")
        
    #     self.fight_text("\nGame Over")
    #     self.fight_text("Click START/CONTINUE to play again.")
    #     self.startButton.clicked.connect(lambda: self.run())

    # def attack(self):
    #     hero_attack_randomized = random.randint(0,2)
    #     if hero_attack_randomized == 0:
    #         self.fight_text(self.hero, "attacks with", self.character_dict[self.hero]["Attack"][0][0])
    #         damage = self.character_dict[self.hero]["Attack"][0][1]
    #     elif hero_attack_randomized == 1:
    #         self.fight_text(self.hero, "attacks with", self.character_dict[self.hero]["Attack"][1][0])
    #         damage = self.character_dict[self.hero]["Attack"][1][1]
    #     elif hero_attack_randomized == 2:
    #         self.fight_text(self.hero, "attacks with", self.character_dict[self.hero]["Attack"][2][0])
    #         damage = self.character_dict[self.hero]["Attack"][2][1]
    #     if random.random() > 0.8:
    #         damage += random.choice([1,2,3,4])
    #         self.fight_text("\nCritical hit!\n")
    #     elif random.random() < 0.05:
    #         self.fight_text(self.hero, "misses.")
    #         damage = 0
    #     return(damage)

    # def item(self):
    #     boar_meat = int(self.character_dict[self.hero]["Item"]["Boar Meat"])
    #     self.fight_text(f"Herakles has ({boar_meat}) Boar Meat")
    #     item_prompt = input("Use item: Boar Meat (y/n) ").strip().lower()
    #     while item_prompt not in ["y","yes","n","no"]:
    #         item_prompt = input("Use item: Boar Meat (y/n) ").strip().lower()
    #     if item_prompt == 'y' or item_prompt == 'yes':
    #         if boar_meat > 0:
    #             boar_meat -= 1
    #             self.character_dict[self.hero]["Item"]["Boar Meat"] = boar_meat
    #             return(44, boar_meat, False)
    #         elif boar_meat <= 0:
    #             boar_meat = 0
    #             self.fight_text("You have no boar meat.\n")
    #             return(0, boar_meat, True)
    #     else:
    #         return(0, boar_meat, True)     
        
    # def random_attack(self, boss, dead):
        
    #     attack_int = random.randint(0,1)
    #     if dead == False:
    #         if attack_int == 0:
    #             self.fight_text(boss, "attacks with", self.character_dict[boss]["Attack"][0][0])
    #             damage = self.character_dict[boss]["Attack"][0][1]
    #         else:
    #             self.fight_text(boss, "attacks with", self.character_dict[boss]["Attack"][1][0])
    #             damage = self.character_dict[boss]["Attack"][1][1]
    #         if random.random() < 0.05:
    #             self.fight_text(boss, "misses.")
    #             damage = 0
    #     else:
    #         self.fight_text("With their last dying breath.....")
            
    #         if random.random() < 0.5:
    #             self.fight_text(boss, "lunges at you, but you dodge the blow easily.")
    #             damage = 0
    #         else:
    #             if attack_int == 0:
    #                 self.fight_text(boss, "attacks with", self.character_dict[boss]["Attack"][0][0])
    #                 damage = self.character_dict[boss]["Attack"][0][1]
    #             else:
    #                 self.fight_text(boss, "attacks with", self.character_dict[boss]["Attack"][1][0])
    #                 damage = self.character_dict[boss]["Attack"][1][1]
    #             if random.random() < 0.05:
    #                 self.fight_text(boss, "misses.")
    #                 damage = 0
    #     return(damage)

    # def boss_fight(self, boss):
    #     dead = False
        
    #     hero_health = int(self.character_dict[self.hero]["Health"])
    #     boss_health = int(self.character_dict[boss]["Health"])
    #     defense = self.character_dict[self.hero]["Defense"]
    #     self.fight_text(f"You are in a boss fight vs {boss}")
    #     self.hero_LCD.setProperty("intValue", hero_health)
    #     self.boss_LCD.setProperty("intValue", boss_health)
    #     self.fight_text("\nEnter a command: (A)ttack or (I)tem")
    #     while (boss_health > 0) and (hero_health > 0):
    #         action = input("Choose an action: ").strip().lower()
    #         while action not in ["attack","a","item","i"]:
    #             action = input("Choose an action: (A)ttack or (I)tem ").strip().lower()
    #         if action == "attack" or action == "a":
    #             attack_damage = self.attack()
    #             boss_health -= attack_damage
                
    #             self.fight_text(f"{self.hero} inflicts {attack_damage} damage")
    #             if boss_health <= 0:
    #                 dead = True
    #             hero_damaged = self.random_attack(boss, dead)
    #             hero_health = (hero_health - hero_damaged) + defense
                
    #             self.fight_text(f"{boss} inflicts {hero_damaged} damage")
    #             if hero_health <= 0:
    #                 self.hero_LCD.setProperty("intValue", 0)
    #             else:
    #                 self.hero_LCD.setProperty("intValue", hero_health)
    #             if boss_health <= 0:
    #                 self.boss_LCD.setProperty("intValue", 0)
    #             else:
    #                 self.boss_LCD.setProperty("intValue", boss_health)

    #         elif action == "item" or action == "i":
    #             item_effect, boar_meat, ambush = self.item()
    #             hero_health += item_effect
    #             if hero_health >= 100:
    #                 hero_health = 100
                
    #             self.fight_text(self.hero, "is healed +", item_effect, "HP")
                
    #             self.fight_text("You have", boar_meat, "Boar Meat(s) left.\n")
    #             if ambush == True:
    #                 self.fight_text("While checking your inventory")
                    
    #                 self.fight_text("you are ambushed.\n")
    #             hero_damaged = self.random_attack(boss, dead)
    #             hero_health = (hero_health - hero_damaged) + defense
                
    #             self.fight_text(boss, "inflicts", hero_damaged, "damage\n")
                
    #             if hero_health <= 0:
    #                 self.fight_text(self.hero, "HP: ", 0)
    #             else:
    #                 self.fight_text(self.hero, "HP: ", hero_health)
                
    #             if boss_health <= 0:
    #                 self.fight_text(boss, "HP: ", 0)
    #             else:
    #                 self.fight_text(boss, "HP: ", boss_health)
    #     self.character_dict[self.hero]["Health"] = hero_health
    #     if (boss_health <= 0) and (hero_health <= 0):
    #         self.both_die(boss)
    #     elif (boss_health <= 0):
    #         self.victory(boss)
    #     else:
    #         self.death(boss)





