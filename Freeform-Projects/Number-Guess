"""1. Roll a pair of dice
2. Add the values of the roll
3. Ask the user to guess a number
4. Compare the user's guess to the total value
5. Determine the winner"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Please insert your guess: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("The maximum value is %d" % (max_val))
  guess = get_user_guess()
  if guess > max_val:
    print("Guess is invalid!")
  else:
    print("Rolling...")
    sleep(2)
    print("The first value is %d" % (first_roll))
    sleep(1)
    print("The second value is %d" % (second_roll))
    sleep(1)
    total_roll = first_roll + second_roll
    print("Result...")
    sleep(1)
    print("The total value is %d" % (total_roll))
    if guess > total_roll:
      print("Your guess is too high")
    elif guess < total_roll:
      print("Your guess is too low")
    else:
      print("You won!")
roll_dice(6)    
