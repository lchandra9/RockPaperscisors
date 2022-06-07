import random


def main():
    print("Welcome to the game")
    Player1 = int(input ("Enter 0 for Rock, 1 for paper, 2 for Scissors")) # it is asking for a rock paper or scissors
    Player2 = random.randint(0, 2)
    if Player1 == 0 and Player2 == 1:
        print("You lose paper covers scissors")
    elif Player1 == 1 and Player2 == 2:
        print("You loose scissors cuts paper")
    elif Player1 == 2 and Player2 == 0:
        print("You loose rock crushes scissors") # line 8-13 are all scinarios where you loose.
    elif Player1 == 1 and Player2 == 0:
        print("You win paper covers scissors")
    elif Player1 == 2 and Player2 == 1:
        print("You win scissors cuts paper")
    elif Player1 == 0 and Player2 == 2:
        print("You win rock crushes scissors") # 14-19 are all scinarios where you win
    else:
        print("Tie")  # If you fon't win or loose then it gives you a tie  
        
        
if __name__ == '__main__':
    main()