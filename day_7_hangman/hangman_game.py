#!/usr/bin/env
import random

letter_bank = []
lives = 6
end_of_game = False

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

from hangman_art import stages
from hangman_art import logo
print(logo)


#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for let in chosen_word:
  display.append("_")

# While loop - guess until you win or lose
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  
  # prompt telling player if he's already guessed the letter. No penalty.
  if guess in display or guess in letter_bank:
      print(f'You\'ve already guessed {guess}.')
      print(' '.join(display))
      continue

  #Check guessed letter
  for i, letter in enumerate(chosen_word):
    if letter == guess:
      display[i] = letter
  
  print(' '.join(display))

# Lose a life for wrong guess
  if (guess not in chosen_word) & (guess not in letter_bank):
    lives -= 1
    letter_bank.append(guess)
    print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
    print(stages[lives])
  
  if "_" not in display:
    end_of_game = True
    print('You win!')

  if lives == 0:
    end_of_game = True
    print('You lose.')
