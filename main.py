import random

class Hero:
    def __init__(self, hp: int, x: list[str]):
        self.health = hp
        self.inventory = x

    def health_check(self):
        if 'Health Potion' in self.inventory:
            self.health += 2
            self.inventory.remove('Health Potion')
            print(f"You used a Health Potion! Your health is now: {self.health}")
        else:
            print("You have no Health Potions left!")

    def death(self):
        if self.health <= 0:
            print("Your health reached 0 and you died.")
            print("\nGAME OVER")
            exit()

    def roll_dice(self) -> int:
        roll = random.randint(1, 6)
        if 'Magic Sword' in self.inventory:
            roll += 1
        return roll

def fight_or_flee() -> str:
    while True:
        choice = input("Do you fight or flee? (fight/flee): ").strip().lower()
        if choice in ['fight', 'flee']:
            return choice
        print("Invalid input. Please enter 'fight' or 'flee'.")

def treasure_choice() -> str:
    while True:
        choice = input("Do you want to open it? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            return choice
        print("Invalid input. Please enter 'y' or 'n'.")

# Game setup
event = ['Monster', 'Treasure', 'Trap']
treasure_list = ['Health Potion', 'Gold', 'Magic Sword', 'Trap']
monster_list = ['Goblin', 'Orc', 'Skeleton']

num_rooms = random.randint(3, 10)
my_inventory = []
my_hero = Hero(10, my_inventory)

print("\nWelcome to the Dungeon!")
print("You are a brave hero on a quest to find treasure and defeat monsters.")
print("You will explore a dungeon with a series of rooms.")

for i in range(num_rooms):
    my_event = random.choice(event)
    print(f"\nRoom {i + 1}:")

    if my_event == 'Monster':
        print(f"You encountered a {random.choice(monster_list)}!")
        my_choice = fight_or_flee()
        roll = my_hero.roll_dice()

        if my_choice == 'fight':
            if roll >= 4:
                print(f"\nYou rolled a {roll} and defeated the monster! No damage taken.")
            elif roll >= 2:
                print(f"\nYou rolled a {roll} and the monster hit you! You flee and take 1 damage.")
                my_hero.health -= 1
                my_hero.health_check()
                my_hero.death()
            else:
                print(f"\nYou rolled a {roll} and the monster hit you hard! You flee and take 2 damage.")
                my_hero.health -= 2
                my_hero.health_check()
                my_hero.death()

        elif my_choice == 'flee':
            if roll >= 5:
                print(f"\nYou rolled a {roll} and fled successfully, ninja style!")
            elif roll > 3:
                print(f"\nYou rolled a {roll} and escaped with a scratch! You take 1 damage.")
                my_hero.health -= 1
                my_hero.health_check()
                my_hero.death()
            elif roll > 1:
                print(f"\nYou rolled a {roll} and got past the monster, but it cost you! You take 2 damage.")
                my_hero.health -= 2
                my_hero.health_check()
                my_hero.death()
            else:
                print(f"\nYou rolled a {roll} and barely escaped! You take 3 damage.")
                my_hero.health -= 3
                my_hero.health_check()
                my_hero.death()

    elif my_event == 'Treasure':
        print("You found a treasure chest!")
        my_choice = treasure_choice()
        if my_choice == 'y':
            my_treasure = random.choice(treasure_list)
            if my_treasure == 'Trap':
                print("\nIt was a trap! You take 2 damage.")
                my_hero.health -= 2
                my_hero.health_check()
                my_hero.death()
            else:
                print(f"\nYou found a {my_treasure}!")
                my_hero.inventory.append(my_treasure)
                print(f"Your inventory: {my_hero.inventory}")
        else:
            print("You chose to leave the chest unopened.")

    else:  # Trap
        print("You stumbled upon a trap!")
        roll = my_hero.roll_dice()
        if roll >= 4:
            print(f"\nYou rolled a {roll} and avoided the trap! Close call!")
        elif roll >= 2:
            print(f"\nYou rolled a {roll} and got hit by a bolt! You take 2 damage.")
            my_hero.health -= 2
            my_hero.health_check()
            my_hero.death()
        else:
            print(f"\nYou rolled a {roll} and fell into a pit! There’s no way out.")
            print("\nGAME OVER")
            exit()

# End of dungeon
print(f"\nYou have explored all {num_rooms} rooms of the dungeon!")
print("Congratulations! You have completed the dungeon!")
print(f"Your final health is: {my_hero.health}")
print(f"Your loot: {my_hero.inventory}")