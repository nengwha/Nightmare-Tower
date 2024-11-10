# Nightmare Tower Game by Whann Eugenio
# November 9, 2024
key = False 
sword = False

def key(obtained): 
    global key
    key = obtained

def sword(obtained):
    global sword
    sword = obtained

def main_menu():
    print("Welcome to the Tower of Nightmare!")
    print("1. Start Game")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        firstfloor()
    elif choice == "2":
        exit()
    else:
        print("Invalid choice")
        main_menu()

def gameover():
    print("Game Over")
    exit()

def firstfloor():
    print("\nYou are in a dark room.")
    print("There are two doors in front of you.")
    print("\nWhich door do you choose?")
    print("1. Left")
    print("2. Right")
    choice = input("Enter your choice: ")
    if choice == "1":
        firstfloor_left_door()
    elif choice == "2":
        firstfloor_right_door()
    else:
        print("Invalid choice")
        firstfloor()

def firstfloor_left_door():
    print("\nYou enter the left door.")
    print("You see a chest in front of you.")
    print("\nWhat do you do?")
    print("1. Open the chest")
    print("2. Leave the room")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("\nYou open the chest, a monster jumps out")
        print("\nWhat do you do?")
        print("1. Fight")
        print("2. Run")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nYou fight the monster.")
            if sword(True):
                print("You defeated the monster.")
                firstfloor_left_door()
            else:
                print("the monster defeated you.")
                gameover()
        elif choice == "2":
            print("\nYou run away.")
            firstfloor()
        else:
            print("Invalid choice")
            firstfloor_left_door()
        print("Game Over")
        gameover()
    elif choice == "2":
        firstfloor()
    else:
        print("Invalid choice")
        firstfloor_left_door()

def firstfloor_right_door():
    print("\nYou enter the right door.")
    print("You see a staircase in front of you.")
    print("\nWhat do you do?")
    print("1. Go up the staircase")
    print("2. Go back")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("\nYou go up the staircase and reach the next level.")
        floor2()
    elif choice == "2":
        firstfloor()
    else:
        print("Invalid choice")
        firstfloor_right_door()

def floor2():
    print("\nYou are in a well lit room.")
    print("There are two doors in front of you.")
    print("\nWhich door do you choose?")
    print("1. Left")
    print("2. Right")
    choice = input("Enter your choice: ")
    if choice == "1":
        floor2_left_door()
    elif choice == "2":
        floor2_right_door()
    else:
        print("Invalid choice")
        floor2()

def floor2_right_door():
    global key, sword
    print("\nYou enter the left door.")
    print("You see two chests in front of you.")
    print("\nWhat do you do?")
    print("1. Open the first chest")
    print("2. Open the second chest")
    print("3. Leave the room")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("\nYou open the chest")
        print("You found a strange key")
        key(obtained=True)
        key = True
        print("\nWhat do you do?")
        print("1. Open the second chest")
        print("2. Leave the room")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nYou open the chest")
            print("You found a sword")
            sword(obtained=True)
            sword = True
            print("\nWhat do you do?")
            print("1. Leave the room")
            choice = input("Enter your choice: ")
            if choice == "1":
                floor2()
            else:
                print("Invalid choice")
                floor2_right_door()
        elif choice == "2":
            floor2()
        else:
            print("Invalid choice")
            floor2_right_door()
    elif choice == "2":
        print("\nYou open the chest")
        print("You found a sword")
        sword(obtained=True)
        sword = True
        print("\nWhat do you do?")
        print("1. Open the first chest")
        print("2. Leave the room")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nYou open the chest")
            print("You found a strange key")
            key(obtained=True)
            key = True
            print("\nWhat do you do?")
            print("1. Leave the room")
            choice = input("Enter your choice: ")
            if choice == "1":
                floor2()
            else:
                print("Invalid choice")
                floor2_right_door()
        elif choice == "2":
            floor2()
        else:
            print("Invalid choice")
            floor2_right_door()
    elif choice == "3":
        floor2()
    else:
        print("Invalid choice")
        floor2_right_door()

def floor2_left_door():
    print("\nYou enter the right door.")
    print("A monster appears in front of you.")
    print("\nWhat do you do?")
    print("1. Fight")
    print("2. Run")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("\nYou fight the monster.")
        if sword == True:
            print("You defeated the monster.")
            print("\nYou find a door behind the monster.")
            print("\nWhat do you do?")
            print("1. Open the door")
            print("2. Leave the room")
            choice = input("Enter your choice: ")
            if choice == "1":
                if key == True:
                    print("\nYou open the door and find a staircase.")
                    print("You go up the staircase and reach the next level.")
                    floor3()
                else:
                    print("\nYou open the door but it is locked.")
                    print("\nWhat do you do?")
                    print("1. Go back")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        floor2()
            elif choice == "2":
                print("\nYou leave the room.")
                floor2()
            else:
                print("Invalid choice")
                floor2_left_door()
        else:
            print("The monster defeated you.")
            gameover()
    elif choice == "2":
        print("\nYou run away.")
        floor2()
    else:
        print("Invalid choice")
        floor2_left_door()

def floor3():
    print("\nYou have reached the top floor.")
    print("You see a chest in front of you.")
    print("\nWhat do you do?")
    print("1. Open the chest")
    print("2. Leave the room")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("\nYou open the chest.")
        print("You found the treasure!")
        print("Congratulations! You have completed the game.")
        exit()
    elif choice == "2":
        floor2()
    else:
        print("Invalid choice")
        floor3()

main_menu()