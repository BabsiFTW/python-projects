"""1. Prompt the user to select either Rock, Paper, Scissors
2. Instruct the computer to randomly select either Rock, Paper or Scissors
3. Compare the user's choice and the computer's choice
4. Determine a winner
5. Inform the user who the winner is"""
from random import randint
options = ["Rock", "Paper", "Scissors"]
message = {
  "tie":"Yawn it's a tie", 
  "won":"Yay you won!", 
  "lost":"Aw you lost!"
}

def decide_winner(user_choice, computer_choice):
  print "This is your choice: %s" % user_choice
  print "This is the computer's choice: %s" % computer_choice
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == "Scissors" and computer_choice == "Paper":
    print message["won"]
  elif user_choice == "Paper" and computer_choice == "Rock":
    print message["won"]
  else:
    print message["lost"]
    
def play_RPS():#
  user_choice = raw_input("Choose your weapon: Rock, Paper or Scissors! ")
  #user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)

play_RPS()
