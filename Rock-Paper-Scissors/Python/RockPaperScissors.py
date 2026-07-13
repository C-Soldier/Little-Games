import random as r

while True:
    computer_rps = r.choice(['rock', 'paper', 'scissors'])

    user_rps = input("type rock, paper or scissors: ")


    if computer_rps.lower() == user_rps.lower():
        print(f"""COMPUTER:{computer_rps}
YOU:{user_rps} 
TIE""")
    elif computer_rps.lower() == 'rock' and user_rps.lower() == 'scissors':
        print(f"""COMPUTER:{computer_rps}
YOU:{user_rps} 
COMPUTER WINS""")

    elif computer_rps.lower() == 'rock' and user_rps.lower() == 'paper':
        print(f"""COMPUTER:{computer_rps}
YOU:{user_rps} 
YOU WIN""")

    elif computer_rps.lower() == 'paper' and user_rps.lower() == 'rock':
        print(f"""COMPUTER:{computer_rps}
YOU:{user_rps} 
COMPUTER WINS""")
        
    elif computer_rps.lower() == 'paper' and user_rps.lower() == 'scissors':
        print(f"""COMPUTER:{computer_rps}
YOU:{user_rps} 
YOU WIN""")

    elif computer_rps.lower() == 'scissors' and user_rps.lower() == 'paper':
        print(f"""COMPUTER:{computer_rps}
YOU:{user_rps} 
COMPUTER WINS""")

    elif computer_rps.lower() == 'scissors' and user_rps.lower() == 'rock':
        print(f"""COMPUTER:{computer_rps}
YOU:{user_rps} 
YOU WIN""")
    
    else:
        print("INVALID")
