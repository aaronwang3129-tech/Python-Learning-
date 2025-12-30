import random

def main_menu():
    print()
    print("-----------------------------------"
          "\nWelcome to the Text Based RPG Game!"
          "\n-----------------------------------"
          "\n1. Play Game"
          "\n2. Exit Game"
          "\n-----------------------------------")
    while True:
        user_input = input("Select an option(1,2,3): ")
        if user_input == "1":
            start_game()
        elif user_input == "2":
            return
        else:
            print("Please select a valid option")

def character_selection():
    print()
    print("-----------------------------------"
          "\nChoose a class!"
          "\n-----------------------------------"
          "\n1. Warrior"
          "\n2. Thief"
          "\n3. Mage"
          "\n4. Class Info"
          "\n5. Return to Main Menu"
          "\n-----------------------------------")
    while True:
        class_choice = input("Select an option: ")
        if class_choice == "5":
            main_menu()
        elif class_choice in ["1" , "2", "3"]:
            return class_choice
        elif class_choice == "4":
            class_info()
        else:
            print("Please select a valid option")

class Class:
    def __init__(self, character_class):
        self.character_class = character_class
        self.level = 1
        self.user_coins = 3
        if character_class == "1":
            self.user_class = "Warrior"
            self.health = 100
            self.agility = 35
            self.stamina = 75
            self.moveset = (""
                            "\nSlice (DMG:15) (75% Hit Rate) (STM:10)"
                            "\nFlourish (DMG:35) (65% Hit Rate) (STM:25)"
                            "\nOverhead (DMG:50) (35% Hit Rate) (STM:45)")
            self.move1_name = "Slice"
            self.move2_name = "Flourish"
            self.move3_name = "Overhead"
            self.move1 = "Slice (DMG:15) (80% Hit Rate) (STM:10)"
            self.move2 = "Flourish (DMG:35) (75% Hit Rate) (STM:25)"
            self.move3 = "Overhead (DMG:50) (50% Hit Rate) (STM:45)"
            self.move1_damage = 15
            self.move2_damage = 35
            self.move3_damage = 50
            self.move1_stamina = 10
            self.move2_stamina = 25
            self.move3_stamina = 45
            self.move1_hit_rate = 80
            self.move2_hit_rate = 75
            self.move3_hit_rate = 50
        elif character_class == "2":
            self.user_class = "Thief"
            self.health = 85
            self.agility = 50
            self.stamina = 90
            self.moveset = (""
                            "\nSlash (DMG:10) (85% Hit Rate) (STM:15)"
                            "\nRapid Slash (DMG:30) (60% Hit Rate) (STM:35)"
                            "\nBack Stab (DMG:45) (33% Hit Rate) (STM:55)")
            self.move1_name = "Slash"
            self.move2_name = "Rapid Slash"
            self.move3_name = "Back Stab"
            self.move1= "Slash (DMG:10) (85% Hit Rate) (STM:15)"
            self.move2 = "Rapid Slash (DMG:30) (70% Hit Rate) (STM:35)"
            self.move3 = "Back Stab (DMG:45) (33% Hit Rate) (STM:55)"
            self.move1_damage = 10
            self.move2_damage = 30
            self.move3_damage = 45
            self.move1_stamina = 15
            self.move2_stamina = 35
            self.move3_stamina = 55
            self.move1_hit_rate = 85
            self.move2_hit_rate = 70
            self.move3_hit_rate = 33
        elif character_class == "3":
            self.user_class = "Mage"
            self.health = 75
            self.agility = 25
            self.stamina = 80
            self.moveset = (""
                            "\nMagic Ball (DMG:20) (70% Hit Rate) (STM:20)"
                            "\nElemental Effect (DMG:15) (60% Hit Rate) (STM:30) (Random Effect)"
                            "\nPotion Conjur (STM:25) (Random Potion)")
            self.move1_name = "Magic Ball"
            self.move2_name = "Elemental Effect"
            self.move3_name = "Potion Conjur"
            self.move1 = "Magic Ball (DMG:20) (80% Hit Rate) (STM:20)"
            self.move2 = "Elemental Effect (DMG:15) (70% Hit Rate) (STM:30) (Random Effect)"
            self.move3 = "Potion Conjur (STM:25) (Random Potion)"
            self.move1_damage = 20
            self.move2_damage = 15
            self.move1_stamina = 20
            self.move2_stamina = 30
            self.move3_stamina = 25
            self.move1_hit_rate = 80
            self.move2_hit_rate = 70
            self.move3_hit_rate = 100

        self.health_cost = 1
        self.health_stock = 2
        self.health_amount = 0
        self.stamina_cost = 1
        self.stamina_stock = 2
        self.stamina_amount = 0
        self.rage_cost = 1
        self.rage_stock = 2
        self.rage_amount = 0
        self.weapon_cost = 2
        self.weapon_stock = 1
        self.weapon_amount = 0
        self.armor_cost = 2
        self.armor_stock = 1
        self.armor_amount = 0

        self.battle_console = "Yolo"

        self.ventura_fiend_move1 = "Fireball"
        self.ventura_fiend_move1_damage = 20
        self.ventura_fiend_move1_stamina = 25
        self.ventura_fiend_move2 = "Claw"
        self.ventura_fiend_move2_damage = 15
        self.ventura_fiend_move2_stamina = 20
        self.ventura_fiend_move3 = "Scream"
        self.ventura_fiend_move3_damage = 15
        self.ventura_fiend_move3_stamina = 10
        self.ventura_fiend_health = 125
        self.ventura_fiend_agility = 45
        self.ventura_fiend_stamina = 75
        self.ventura_fiend_move1_hit_rate = 20
        self.ventura_fiend_move2_hit_rate = 25
        self.ventura_fiend_move3_hit_rate = 15


    def stats(self):
        print()
        print("-----------------------------------"
              "\nStats"
              "\n-----------------------------------")
        print(f"Class: {self.user_class}"
              f"\nHealth: {self.health}"
              f"\nAgility: {self.agility}"
              f"\nStamina: {self.stamina}"
              f"\nMoveset: {self.moveset}"
              "\n-----------------------------------"
              "\n1. Confirm Stats"
              "\n2. Return to Main Menu"
              "\n-----------------------------------")
        while True:
            user_input = input("Select an option: ")
            if user_input == "2":
                main_menu()
            elif user_input == "1":
                self.starter_cutscenes()
            else:
                print("Please select a valid option")

    def starter_cutscenes(self):
        print()
        print("-----------------------------------"
              "\nA long time ago the Kingdom of Vinland and the"
              "\nLand of Ventura lived in harmony..."
              "\n-----------------------------------"
              "\n1. Continue"
              "\n2. Skip"
              "\n-----------------------------------")
        self.starter_cutscenes_continue()
        print()
        print("-----------------------------------"
              "\nUntil the Creatures of Ventura attacked."
              "\nThey wanted more power than the humans..."
              "\n-----------------------------------"
              "\n1. Continue"
              "\n2. Skip"
              "\n-----------------------------------")
        self.starter_cutscenes_continue()
        print()
        print("-----------------------------------"
              "\nThe Creatures of Ventura now reside in dungeons."
              "\nUsing these dungeons as an area to feast on the citizens..."
              "\n-----------------------------------"
              "\n1. Continue"
              "\n-----------------------------------")
        while True:
            user_input = input("Select an option: ")
            if user_input == "1":
                self.starter_location()
            elif user_input == "2":
                self.starter_location()
            else:
                print("Please select a valid option")

    def starter_cutscenes_continue(self):
        while True:
            user_input = input("Select an option: ")
            if user_input == "1":
                break
            elif user_input == "2":
                self.starter_location()
            else:
                print("Please select a valid option")

    def starter_location(self):
        print()
        print("-----------------------------------"
              f"\nWelcome to Vinland..."
              "\n-----------------------------------"
              f"\nYou start your journey as a {self.user_class}..."
              "\n-----------------------------------"
              "\n1. Head to a Dungeon"
              "\n2. Visit the Shops"
              "\n3. Explore the Area"
              "\n-----------------------------------")
        while True:
            user_input = input("Select an option: ")
            if user_input == "1":
                self.start_parth_dungeon()
            elif user_input == "2":
                self.shops()
            elif user_input == "3":
                self.explore()
            else:
                print("Please select a valid option")

    def explore(self):
        print("-----------------------------------"
              "\nVinland"
              "\n-----------------------------------"
              "\nYou search the area."
              "\nTowns and trees are burning all around you."
              "\n-----------------------------------"
              "\n1. Continue Exploring"
              "\n2. Head Back"
              "\n-----------------------------------")
        self.explore_continue()
        print("-----------------------------------"
              "\nVinland"
              "\n-----------------------------------"
              "\nYou go closer where the dungeons reside."
              "\nBlood trails smeared everywhere you look."
              "\n-----------------------------------"
              "\n1. Continue Exploring"
              "\n2. Head Back"
              "\n-----------------------------------")
        self.explore_continue()
        print("-----------------------------------"
              "\nVinland"
              "\n-----------------------------------"
              "\nYou go even closer and your heart starts pumping."
              "\nA Creature is patrolling the area..."
              "\n-----------------------------------"
              "\n1. Enter the Dungeon"
              "\n2. Head Back"
              "\n-----------------------------------")
        while True:
            user_input = input("Select an option: ")
            if user_input == "1":
                self.start_parth_dungeon()
            elif user_input == "2":
                self.starter_location()
            else:
                print("Please select a valid option")

    def explore_continue(self):
        while True:
            user_input = input("Select an option: ")
            if user_input == "1":
                break
            elif user_input == "2":
                self.starter_location()
            else:
                print("Please select a valid option")

    def shops(self):
        print()
        print("-----------------------------------"
              "\nShops"
              "\n-----------------------------------"
              f"\n1. $1 - Health Potion (Stock: {self.health_stock})"
              f"\n2. $1 - Stamina Potion (Stock: {self.stamina_stock})"
              f"\n3. $1 - Rage Potion (Stock: {self.rage_stock})"
              f"\n4. $2 - Weapon Upgrade (Stock: {self.weapon_stock})"
              f"\n5. $2 - Armor Upgrade (Stock: {self.armor_stock})"
              "\n6. Check Inventory"
              "\n7. Go Back"
              f"\n Coin Balance: {self.user_coins}"
              "\n-----------------------------------")
        while True:
            user_input = input("Select an option: ")
            if user_input == "1" and self.user_coins > 0 and self.health_stock > 0:
                self.user_coins -= self.health_cost
                self.health_stock -= 1
                self.health_amount += 1
                print("-----------------------------------"
                      "\nYou purchased 1 Health Potion!"
                      "\n-----------------------------------")
            elif user_input == "2" and self.user_coins > 0 and self.stamina_stock > 0:
                self.user_coins -= self.stamina_cost
                self.stamina_stock -= 1
                self.stamina_amount += 1
                print("-----------------------------------"
                      "\nYou purchased 1 Stamina Potion!"
                      "\n-----------------------------------")
            elif user_input == "3" and self.user_coins > 0 and self.rage_stock > 0:
                self.user_coins -= self.rage_cost
                self.rage_stock -= 1
                self.rage_amount += 1
                print("-----------------------------------"
                      "\nYou purchased 1 Rage Potion!"
                      "\n-----------------------------------")
            elif user_input == "4" and self.user_coins > 0 and self.weapon_stock > 0:
                self.user_coins -= self.weapon_cost
                self.weapon_stock -= 1
                self.weapon_amount += 1
                print("-----------------------------------"
                      "\nYou purchased Weapon Upgrade!"
                      "\n-----------------------------------")
            elif user_input == "5" and self.user_coins > 0 and self.armor_stock > 0:
                self.user_coins -= self.armor_cost
                self.armor_stock -= 1
                self.armor_amount += 1
                print("-----------------------------------"
                      "\nYou purchased Armor Upgrade!"
                      "\n-----------------------------------")
            elif user_input == "6":
                self.inventory()
            elif user_input == "7":
                self.starter_location()
            else:
                print("Please select a valid option")

    def inventory(self):
        print()
        print("-----------------------------------"
              "\nInventory"
              "\n-----------------------------------")
        if self.health_amount > 0:
            print(f"Health Potions: {self.health_amount}")
        if self.stamina_amount > 0:
            print(f"Agility Potions: {self.stamina_amount}")
        if self.rage_amount > 0:
            print(f"Rage Potions: {self.rage_amount}")
        if self.weapon_amount > 0:
            print(f"Weapon upgrades: {self.weapon_amount}")
        if self.armor_amount > 0:
            print(f"Armor Upgrades: {self.armor_amount}")
        print(f"Coin Balance: {self.user_coins}"
              "\n-----------------------------------"
              "\n1. Shop"
              "\n2. Go Back"
              "\n-----------------------------------")
        while True:
            user_input = input("Select your option: ")
            if user_input == "1":
                print()
                print("-----------------------------------"
                      "\nShops"
                      "\n-----------------------------------"
                      f"\n1. $1 - Health Potion (Stock: {self.health_stock})"
                      f"\n2. $1 - Stamina Potion (Stock: {self.stamina_stock})"
                      f"\n3. $1 - Rage Potion (Stock: {self.rage_stock})"
                      f"\n4. $2 - Weapon Upgrade (Stock: {self.weapon_stock})"
                      f"\n5. $2 - Armor Upgrade (Stock: {self.armor_stock})"
                      "\n6. Check Inventory"
                      "\n7. Go Back"
                      f"\n Coin Balance: {self.user_coins}"
                      "\n-----------------------------------")
                return
            elif user_input == "2":
                self.starter_location()
            else:
                print("Please select a valid option")

    def start_parth_dungeon(self):
        print()
        print("-----------------------------------"
              "\nParth Dungeon"
              "\n-----------------------------------"
              "\nYou enter the dungeon..."
              "\nA Ventura Fiend is guarding the main entrance..."
              "\n-----------------------------------"
              "\n1. Fight the Ventura Fiend"
              "\n2. Go back for now"
              "\n3. Inventory"
              "\n-----------------------------------")
        while True:
            user_input = input("Enter your option: ").lower()
            if user_input == "1":
                self.ventura_fiend_user()
            elif user_input == "2":
                self.starter_location()
            elif user_input == "3":
                self.inventory()

    def ventura_fiend_user(self):
        while True:
            hit_rate = random.randint(1, 100)
            print()
            print("-----------------------------------"
                  "\nBattle 1"
                  "\n-----------------------------------"
                  "\nVentura Fiend (Level 5)"
                  f"\nHealth: {self.ventura_fiend_health}"
                  f"\nAgility: {self.ventura_fiend_agility}"
                  f"\nStamina: {self.ventura_fiend_stamina}"
                  "\n-----------------------------------"
                  f"\n{self.user_class} (Level {self.level})"
                  f"\nHealth: {self.health}"
                  f"\nAgility: {self.agility}"
                  f"\nStamina: {self.stamina}"
                  "\n-----------------------------------"
                  "\n===Moves==="
                  "\n-----------------------------------"
                  f"\nA. {self.move1}"
                  f"\nB. {self.move2}"
                  f"\nC. {self.move3}"
                  "\nD. Inventory"
                  "\nE. Rest")
            user_input = input("Enter your option: ").lower()
            if user_input == "a" and hit_rate <= self.move1_hit_rate and self.stamina >= self.move1_stamina:
                self.stamina -= self.move1_stamina
                self.ventura_fiend_health -= self.move1_damage
                self.battle_console = f"Your {self.move1_name} hit for {self.move1_damage} damage!"
                self.battle_console_user()
            elif user_input == "b" and hit_rate <= self.move2_hit_rate and self.stamina >= self.move2_stamina:
                self.stamina -= self.move2_stamina
                self.ventura_fiend_health -= self.move2_damage
                self.battle_console = f"Your {self.move2_name} hit for {self.move2_damage} damage!"
                self.battle_console_user()
            elif user_input == "c" and hit_rate <= self.move3_hit_rate and self.stamina >= self.move3_stamina:
                self.stamina -= self.move3_stamina
                self.ventura_fiend_health -= self.move3_damage
                self.battle_console = f"Your {self.move3_name} hit for {self.move3_damage} damage!"
                self.battle_console_user()
            elif user_input == "a" and self.stamina <= self.move1_stamina:
                self.battle_console = "Your out of stamina!"
                self.battle_console_user()
            elif user_input == "b" and self.stamina <= self.move2_stamina:
                self.battle_console = "Your out of stamina!"
                self.battle_console_user()
            elif user_input == "c" and self.stamina <= self.move3_stamina:
                self.battle_console = "Your out of stamina!"
                self.battle_console_user()
            elif user_input == "a" and hit_rate >= self.move1_hit_rate:
                self.battle_console = f"Your move {self.move1_name} missed!"
                self.battle_console_user()
            elif user_input == "b" and hit_rate >= self.move2_hit_rate:
                self.battle_console = f"Your move {self.move2_name} missed!"
                self.battle_console_user()
            elif user_input == "c" and hit_rate >= self.move3_hit_rate:
                self.battle_console = f"Your move {self.move3_name} missed!"
                self.battle_console_user()
            elif user_input == "d":
                pass
            elif user_input == "e":
                self.stamina += 20
            else:
                print("Please select a valid option")

    def ventura_fiend_self(self):
        hit_rate = random.randint(1, 100)
        ventura_fiend_move = random.choice(["Fireball", "Claw", "Scream"])
        if ventura_fiend_move == "Fireball" and hit_rate <= 80 and self.ventura_fiend_stamina >= self.ventura_fiend_move1_stamina:
            self.ventura_fiend_stamina -= self.ventura_fiend_move1_stamina
            self.health -= self.ventura_fiend_move1_damage
            self.battle_console = f"The Ventura Fiend's {self.ventura_fiend_move1} hit for {self.ventura_fiend_move1_damage} damage!"
        elif ventura_fiend_move == "Claw" and hit_rate <= 75 and self.ventura_fiend_stamina >= self.ventura_fiend_move2_stamina:
            self.ventura_fiend_stamina -= self.ventura_fiend_move2_stamina
            self.health -= self.ventura_fiend_move2_damage
            self.battle_console = f"The Ventura Fiend's {self.ventura_fiend_move2} hit for {self.ventura_fiend_move2_damage} damage!"
        elif ventura_fiend_move == "Scream" and hit_rate <= 85 and self.ventura_fiend_stamina >= self.ventura_fiend_move3_stamina:
            self.ventura_fiend_stamina -= self.ventura_fiend_move3_stamina
            self.health -= self.ventura_fiend_move3_damage
            self.battle_console = f"The Ventura Fiend's {self.ventura_fiend_move3} hit for {self.ventura_fiend_move3_damage} damage!"
        elif ventura_fiend_move == "Fireball" and self.ventura_fiend_stamina <= self.ventura_fiend_move1_stamina:
            self.battle_console = "The Ventura Fiend is out of stamina!"
        elif ventura_fiend_move == "Claw" and self.ventura_fiend_stamina <= self.ventura_fiend_move2_stamina:
            self.battle_console = "The Ventura Fiend is out of stamina!"
        elif ventura_fiend_move == "Cream" and self.ventura_fiend_stamina <= self.ventura_fiend_move3_stamina:
            self.battle_console = "The Ventura Fiend is out of stamina!"        elif ventura_fiend_move == "Fireball" and hit_rate >= self.ventura_fiend_move1_hit_rate:
            self.battle_console = f"The Ventura Fiend's {self.ventura_fiend_move1} missed!"
        elif ventura_fiend_move == "Fireball" and hit_rate >= self.ventura_fiend_move2_hit_rate:
            self.battle_console = f"The Ventura Fiend's {self.ventura_fiend_move2} missed!"
        elif ventura_fiend_move == "Fireball" and hit_rate >= self.ventura_fiend_move3_hit_rate:
            self.battle_console = f"The Ventura Fiend's {self.ventura_fiend_move3} missed!"
        if self.ventura_fiend_stamina < 25:
            self.ventura_fiend_stamina += 20
            self.battle_console = "The Ventura Fiend rested!"
        self.battle_console_fiend()

    def battle_console_user(self):
        print()
        print("-----------------------------------"
              f"\n{self.battle_console}"
              "\n-----------------------------------"
              "\n1. Continue")
        while True:
            user_input = input("Select your option: ").lower()
            if user_input == "1":
                self.ventura_fiend_self()
            else:
                print("Please select a valid option")

    def battle_console_fiend(self):
        print()
        print("-----------------------------------"
              f"\n{self.battle_console}"
              "\n-----------------------------------"
              "\n1. Continue")
        while True:
            user_input = input("Select your option: ").lower()
            if user_input == "1":
                self.ventura_fiend_user()
            else:
                print("Please select a valid option")

def class_info():
    print()
    print("-----------------------------------"
          "\nClass Info"
          "\n-----------------------------------"
          "\n1. Warrior Info"
          "\n2. Thief Info"
          "\n3. Mage Info"
          "\n4. Main Menu"
          "\n-----------------------------------")
    while True:
        user_input = input("Enter your option: ").lower()
        if user_input == "1":
            warrior_info()
        elif user_input == "2":
            thief_info()
        elif user_input == "3":
            mage_info()
        elif user_input == "4":
            main_menu()
        else:
            print("Please select a valid option")

def warrior_info():
    print()
    print("-----------------------------------"
          "\nWarrior Info"
          "\n-----------------------------------"
          "\nHealth:100"
          "\nAgility:35"
          "\nStamina:75"
          "\nMoveset:"
          "\nSlice! (DMG:15) (75% Hit Rate) (STM:10)"
          "\nFlourish! (DMG:35) (65% Hit Rate) (STM:25)"
          "\nOverhead! (DMG:50) (35% Hit Rate) (STM:45)"
          "\n-----------------------------------"
          "\n1. Class Info"
          "\n2. Main Menu"
          "\n-----------------------------------")
    while True:
        user_input = input("Select an option: ")
        if user_input == "1":
            class_info()
        elif user_input == "2":
            main_menu()
        else:
            print("Please select a valid option")

def thief_info():
    print()
    print("-----------------------------------"
          "\nThief Info"
          "\n-----------------------------------"
          "\nHealth:85"
          "\nAgility:50"
          "\nStamina:90"
          "\nMoveset:"
          "\nSlash! (DMG:10) (85% Hit Rate) (STM:15)"
          "\nRapid Slashes! (DMG:30) (60% Hit Rate) (STM:35)"
          "\nBask Stab! (DMG:45) (33% Hit Rate) (STM:55)"
          "\n-----------------------------------"
          "\n1. Class Info"
          "\n2. Main Menu"
          "\n-----------------------------------")
    while True:
        user_input = input("Select an option: ")
        if user_input == "1":
            class_info()
        elif user_input == "2":
            main_menu()
        else:
            print("Please select a valid option")

def mage_info():
    print()
    print("-----------------------------------"
          "\nMage Info"
          "\n-----------------------------------"
          "\nHealth:75"
          "\nAgility:25"
          "\nStamina:80"
          "\nMoveset:"
          "\nMagic Ball! (DMG:20) (70% Hit Rate) (STM:20)"
          "\nElemental Effect! (DMG:15) (60% Hit Rate) (STM:30) (Random Effect)"
          "\nPotion Conjur! (STM:25) (Random Potion)"
          "\n-----------------------------------"
          "\n1. Class Info"
          "\n2. Main Menu"
          "\n-----------------------------------")
    while True:
        user_input = input("Select an option: ")
        if user_input == "1":
            class_info()
        elif user_input == "2":
            main_menu()
        else:
            print("Please select a valid option")

def start_game():
    while True:
        character_class = character_selection()
        user = Class(character_class)
        user.stats()
        break

main_menu()