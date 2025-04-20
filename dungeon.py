"""Game: Dungeon Dice Game"""

import traceback
import sys
try:
    import random

    class Hero:
        def __init__(self, hp, x):
            self.health = hp
            self.inventory = x
        def health_check(self):
            if 'Health Potion' in self.inventory:
                self.health = self.health + 2
                self.inventory.remove('Health Potion')
                print(f"You used a Health Potion! Your health is now: {self.health}")
                return self.health
            else:
                print("You have no Health Potions left!")
                return self.health
        def death(self):
            if self.health <= 0:
                print("Your health reached 0 and you died.")
                print("\nGAME OVER")
                input("Press enter to exit...")
                sys.exit()
        def roll_dice(self):
            if 'Magic Sword' in self.inventory:
                roll = random.randint(1, 6) + 1
                return roll
            else:
                roll = random.randint(1, 6)
                return roll
            
    def fight_or_flee():
        while True:
            choice = input("Do you fight or flee? (fight/flee): ").strip().lower()
            try:
                if choice == 'fight':
                    print("You are no coward! You choose to fight!")
                    return choice
                elif choice == 'flee':
                    print("Way above your pay grade! You choose to flee!")
                    return choice
            except ValueError:
                print("Invalid input. Please enter 'fight' or 'flee'.")

    def treasure_choice():
        while True:
            choice = input("Do you want to open it? (y/n): ").strip().lower()
            try:
                if choice == 'y':
                    print("You opened the chest!")
                    return "open"
                elif choice == 'n':
                    print("You chose to leave the chest onopened.")
                    return "leave"
            except ValueError:
                print("Invalid input. Please enter either 'y' or 'n'.")

    event = ['Monster', 'Treasure', 'Trap']
    treasure_list = ['Health Potion', 'Gold', 'Magic Sword', 'Trap']
    monster_list = ['Goblin', 'Orc', 'Skeleton']

    num_rooms = random.randint(3, 10)
    my_inventory = []
    my_health = 10
    my_hero = Hero(my_health, my_inventory)

    print("\nWelcome to the Dungeon!")
    print("You are a brave hero on a quest to find treasure and defeat monsters.")
    print("You will explore a dungeon with a series of rooms.")

    for i in range(0, num_rooms, 1):
        my_event = random.choice(event)
        if my_event == 'Monster':
            print(f"\nRoom {i + 1}: You encountered a {random.choice(monster_list)}!")
            my_choice = fight_or_flee()
            if my_choice == 'fight':
                my_roll = my_hero.roll_dice()
                if my_roll >= 4:
                    print(f"\nYou rolled a {my_roll} and defetead the monster! No damage taken.")
                    input("\nPress enter to continue...")
                elif my_roll >= 2 and my_roll < 4:
                    print(f"\nYou rolled a {my_roll} and the moster hit you! You flee and take 1 damage.")
                    my_hero.health = my_hero.health - 1
                    my_hero.death()
                    my_hero.health_check()
                    input("\nPress enter to continue...")
                else:
                    print(f"\nYou rolled a {my_roll} and the moster hit you! You flee and take 2 damages.")
                    my_hero.health = my_hero.health - 2
                    my_hero.death()
                    my_hero.health_check()
                    input("\nPress enter to continue...")
            elif my_choice == 'flee':
                my_roll = my_hero.roll_dice()
                if my_roll >= 5:
                    print(f"\nYou rolled a {my_roll} and successfully fled unnoticed, ninja style!")
                    input("\nPress enter to continue...")
                elif my_roll > 3 and my_roll <= 4:
                    print(f"\nYou rolled a {my_roll} and got past the monster with just a scratch! You take 1 damage.")
                    my_hero.health = my_hero.health - 1
                    my_hero.death()
                    my_hero.health_check()
                    input("\nPress enter to continue...")
                elif my_roll > 1 and my_roll <= 3:
                    print(f"\nYou rolled a {my_roll} and got past the monster but took a beating! You take 2 damages.")
                    my_hero.health = my_hero.health - 2
                    my_hero.death()
                    my_hero.health_check()
                    input("\nPress enter to continue...")
                else:
                    print(f"\nYou rolled a {my_roll} and just barely escaped! You take 3 damages.")
                    my_hero.health = my_hero.health - 3
                    my_hero.death()
                    my_hero.health_check()
                    input("\nPress enter to continue...")
        elif my_event == 'Treasure':
            print(f"\nRoom {i + 1}: You found a treasure chest!")
            my_choice = treasure_choice()
            if my_choice == 'open':
                my_treasure = random.choice(treasure_list)
                if my_treasure == 'Trap':
                    print("\nYou opened the chest but it was booby trapped! You take 2 damages.")
                    my_hero.health = my_hero.health - 2
                    my_hero.death()
                    my_hero.health_check()
                    input("\nPress enter to continue...")
                else:
                    print(f"\nYou found a {my_treasure}!")
                    my_inventory.append(my_treasure)
                    print(f"\nYour inventory: {my_inventory}")
                    input("\nPress enter to continue...")
        else:
            print(f"\nRoom {i + 1}: You stumbled upon a trap!")
            my_roll = my_hero.roll_dice()
            if my_roll >= 4:
                print(f"\nYou rolled a {my_roll} and avoided the trap! Close call, buddy!")
                input("\nPress enter to continue...")
            elif my_roll >= 2 and my_roll < 4:
                print(f"\nYou rolled a {my_roll} and got hit by a bolt! You take 2 damages.")
                my_hero.health = my_hero.health - 2
                my_hero.death()
                my_hero.health_check()
                input("\nPress enter to continue...")
            else:
                print(f"\nYou rolled a {my_roll} and that's really unfortunate! You fall into a pit and unfortunately there's no way out!")
                print("\nGAME OVER")
                input("Press enter to exit...")
                sys.exit()
    print(f"\nYou have explored all {num_rooms} rooms of the dungeon!")

    print("\nCongratulations! You have completed the dungeon!")
    print(f"\nYour final health is: {my_hero.health}")
    print(f"\nBut it was worthy it! This is your loot: {my_inventory}")

    input("\nPress enter to exit...")

except Exception as e:
    print("\nAn error occured:")
    print(str(e))
    print("\n Detailed traceback:")
    traceback.print_exc()
    input("Press enter to exit...")
