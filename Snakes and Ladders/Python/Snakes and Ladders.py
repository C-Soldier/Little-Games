#Imports
from random import randint as rand
from time import sleep as sl

#Variables
start = True
idle_players = {}
moving_players = {}
snakes = {17:10, 54:20,
          62:43, 64:4,
          87:63, 93:20,
          95:20, 99:21}

ladders = {4:10, 9:22,
           20:18, 28:56,
           40:19, 51:16,
           63:18, 71:20}

#This will count how many people will be playing the game
while True:
    try:
        player_count = int(input("Enter the number of players?: "))
        if player_count > 0:
            break #Exit the loop if the number is positive
        else:
            print("Please enter a number greater than zero\n")
            sl(1)
    except ValueError:
            print("That's not a whole number.\n")
            sl(1)
            print("Please try again\n")
    except Exception as e:
            print(f"An unexpected error occurred: {e}.")
            sl(1)
            print("Please try again\n")

#This will let the user type the name of each player to avoid confusion
print("Enter the name of each player")
for player in range(player_count):
    playerName = input(f"Player {player + 1}: ")
    idle_players.update({f"Player {player + 1} - {playerName}": 0})
    sl(1)

#This is used to display each player
for key, value in idle_players.items():
    print(f"{key} :: Square - {value}")
    sl(0.5)

#This is for each player to roll the die
while start:
    #If the player rolls a six they can move on the board
    try: 
        for key, value in idle_players.items():
            input(f"{key}, press enter to roll the die....")
            die = rand(1, 6) #Used to roll the die       
            if die == 6:
                print(f"\nYou rolled a {die}\n")
                sl(1)
                print(f"{key} can move\n")
                sl(1)
                
                input(f"{key}, press enter to roll the die again")
                die = rand(1,6)
                print(f"\nYou rolled a {die}\n")
                value += die
                sl(1)
                print(f"{key} is now on square {value}\n")
                sl(1)
                
                moving_players.update({key: value})
                del idle_players[key]
            else:
                print(f"\nYou rolled a {die}\n")
                sl(1)
                print("Your turn has been skipped\n")
                sl(1)
    except RuntimeError:
        pass
    
    #This is to show the position of each player
    for key, value in sorted(idle_players.items()):
        print(f"{key} :: Square - {value}")
        sl(0.5)
    for key, value in moving_players.items():
        print(f"{key} :: Square - {value}")
        sl(0.5)

    #This is for the players to play the game 
    for key, value in moving_players.items():
        input(f"{key} press enter to roll the die....")
        die = rand(1, 6)
        value += die
        print(f"\nYou rolled a {die}\n")
        sl(1)
        print(f"{key} is now on Square {value}\n")
        sl(1)
        if value > 100:
            value -= die
            moving_players.update({key: value})
            print(f"""{key} has moved passed the 100th Sqaure\n
Roll an exact number to win\n""")
            sl(3)
        #Snakes
        try:
            value -= snakes[value]
            print(f"{key} has landed on a snake\n")
            sl(1)
            print(f"{key} is now on Square {value}\n")
        except KeyError:
            pass
            
        #Ladders
        try:
            value += ladders[value]
            print(f"{key} has landed on a ladder\n")
            sl(1)
            print(f"{key} is now on Square {value}\n")
        except KeyError:
            pass
            
        #This is if the player rolls a six and they get to move again
        while die == 6:
            input(f"{key}, press enter to roll again....")
            die = rand(1, 6)
            value += die
            print(f"\nYou rolled a {die}\n")
            sl(1)
            print(f"{key} is now on Square {value}\n")
            
            if value > 100:
                value -= die
                print(f"""{key} has moved passed the 100th Sqaure\n
Roll and exact number to win\n""")
                break
            sl(1)
        moving_players.update({key: value})
        if value == 100:
            print(f"{key} Wins!!!")
            start = False
            break

