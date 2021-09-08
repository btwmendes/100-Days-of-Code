# This game was designed for replit and uses its clear function.

from art import logo
from replit import clear
import random

def play_game():
  print(logo)
  print()
  print("Welcome to the Number Guessing Game!\n")
  print("I am thinking of a number between 1 and 100.\n")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  secret_number = random.randint(1, 100)
  # print(secret_number)
  if difficulty == 'easy':
    tries = 10
  else:
    tries = 5

  while tries > 0:
    print(f"You have {tries} attempts remaining to guess the number.\n")
    guess = int(input("Make a guess: "))
    if guess < secret_number:
      print("Too low.\n")
      tries -= 1

    elif guess > secret_number:
      print("Too high.\n")
      tries -= 1

    else:
      print(f"Congratulations! You guessed the secret number which was {guess}.\n")
      break
  
  if tries == 0:
    print("You used all of your turns and lost.")
    print(f"The secret number was {secret_number}.")
    play = input("Do you want to play again?: Type 'y' or 'n': ").lower()
  else:
    play = input("Do you want to play again?: Type 'y' or 'n': ").lower()
  
  if play == 'y':
    clear()
    play_game()


play_game()
