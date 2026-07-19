import random as rand
import os

def clear_terminal():
    # 'nt' means Windows, otherwise it's likely Linux or macOS
    os.system('cls' if os.name == 'nt' else 'clear')

# NOTE: when editing use all caps
words = open("words.txt", "r").read().splitlines()

word = tuple(rand.choice(words))
guess_word = []
letters_guessed = []
tries = 6

for x in range(len(word)):
    guess_word.append("_")

print(guess_word)

while True:
    if tries == 6:
        print("""
|----|      
|      
|  
|    
      """)
        
    elif tries == 5:
        print("""
|----|      
|    O  
|  
|    
      """)
    
    elif tries == 4:
        print("""
|----|      
|    O  
|   [ ]   
|    
      """)
    
    elif tries == 3:
        print("""
|----|      
|    O  
|  |[ ]   
|    
      """)
    
    elif tries == 2:
        print("""
|----|      
|    O  
|  |[ ]|   
|    
      """)
    
    elif tries == 1:
        print("""
|----|      
|    O  
|  |[ ]|   
|   | 
      """)

    guess = input("Enter a letter or guess the word: ")
    clear_terminal()
    
    if (len(guess.upper()) == 1) and (guess.upper() in letters_guessed):
        print(f"You already guessed {guess.upper()}")
        guess = ""
    
    elif (len(guess.upper()) == 1) and (guess.upper() not in word) and (guess.upper() not in letters_guessed):
        tries -= 1
        letters_guessed.append(guess.upper())
        print(f"There are no {guess.upper()}s in the word")
        print(f"You have {tries} tries left")
        guess = ""
    
    elif (len(guess.upper()) > 1) and (tuple(guess.upper()) != word):
        tries -= 1
        print(f"{guess.upper()} is not the word")
        print(f"You have {tries} tries left")
        guess = ""
    
    elif guess == "":
        print("You didnt enter anything")
    
    elif guess.upper() in word and guess.upper() not in letters_guessed:
        letters_guessed.append(guess.upper())
        
        for x in range(len(word)):
            if guess.upper() == word[x]:
                guess_word[x] = guess.upper()
        print(f"{guess} is in the word {word.count(guess.upper())} time(s)")
        print(guess_word)

    elif tuple(guess.upper()) == word:
        print("You got it")
        print(f"The word is {word}")
        break

    if tries == 0 and guess.upper() not in word:
        print("""
|----|      
|    O  
|  |[ ]|   
|   | | 
      """)
        print(f"Youre out of tries\nThe word was {word}")
        break
    
    elif tuple(guess_word) == word:
        print("You got it")
        print(f"The word is {word}")
        break
    
