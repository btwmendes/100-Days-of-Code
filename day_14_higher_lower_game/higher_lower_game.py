# Code is intended to run on replit. It uses a replit clear function.

import random
from replit import clear
from art import logo, vs
from game_data import data

def person(x):
  """Generates a new trivia person."""
  num = random.randint(0, 49)
  print(f"Compare {x}: {data[num]['name']}, a {data[num]['description']} from {data[num]['country']}.\n")
  return data[num]['follower_count']

def check_guess(a, b, user_guess):
  """Check the user input against the data to see if they got it right"""
  if a > b and user_guess == 'A':
    return True
  elif a < b and user_guess == 'B':
    return True
  else:
    return False

def play_game():
  """Loops through the game"""
  tally = 0
  right_answer = True
  while right_answer:
    print(logo)
    person_a = person('A')
    print(vs)
    person_b = person('B')

    guess = input("Who has more followers? Type 'A' or 'B' ").upper()

    win = check_guess(person_a, person_b, guess)
    if win == True:
      clear()
      tally += 1
      print(f"You're right! Current score: {tally}.\n")
    else:
      right_answer = False
      print(f"Sorry, that's wrong. Final score: {tally}.\n")
      play_again = input("Do you want to play again? Type 'Y' or 'N': ").upper()
      if play_again == 'Y':
        clear()
        play_game()

play_game()
