#!/usr/bin/env python3

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

# player inputs move
player = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

# print the player's hand
if player == 0:
  print(rock)
elif player == 1:
  print(paper)
elif player == 2:
  print(scissors)
else:
  print('You input an invalid number.')

# computer inputs move
computer = random.randint(0,2)

# print the computer's hand
print('Computer chose:')
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
else:
  print(scissors)

# decide the winner
if player == computer:
  print('It\'s a draw.')
elif player == 1 and computer == 0:
  print('You win!')
elif player == 2 and computer == 1:
  print('You win!')
elif player == 0 and computer == 2:
  print('You win!')
elif player >= 3 or player < 0:
  print('You input an invalid number. You lose.')
else:
  print('You lose :P')
