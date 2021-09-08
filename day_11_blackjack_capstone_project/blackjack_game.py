#this program should be run on the replit website. It requires the replit clear function. 

import random
from replit import clear
from art import logo

def deal(cards):
  user_hand = []
  dealer_hand = []
  # 2 cards for the player
  user_hand.append(random.choice(cards))
  user_hand.append(random.choice(cards))
  # 2 cards for the dealer
  dealer_hand.append(random.choice(cards))
  dealer_hand.append(random.choice(cards))
  return user_hand, dealer_hand

def card_total(player, dealer):
  user_total = sum(player)
  dealer_total = sum(dealer)
  return user_total, dealer_total

def blackjack(player, dealer, num_player, num_dealer):
  if player == 21 and len(num_player) == 2:
    player_blackjack = True
  else:
    player_blackjack = False
  if dealer == 21 and len(num_dealer) == 2:
    dealer_blackjack = True 
  else:
    dealer_blackjack = False
  return player_blackjack, dealer_blackjack

def bust_check(user_hand, user_total):
  low_ace = [1 if num == 11 else num for num in user_hand]
  if user_total < 22:
    return True
  elif sum(low_ace) < 22:
    return True
  else:
    return False

def soft_seventeen(card, cards_sum):
  if (11 in card) and (cards_sum == 17) and (len(card) == 2):
    return True
    

def computer_play(hand, total):
  low_ace = [1 if num == 11 else num for num in hand]
  if total >= 17 and total <=21:
    return False
  elif total < 17:
    return True
  elif (sum(low_ace) < 17) and (total > 21):
    return True
  else:
    return False

def winner(final_user_total, final_dealer_total, final_user_hand, final_dealer_hand):
  print(f"Your hand: {final_user_hand}")
  print(f"The dealer: [{final_dealer_hand}\n")
  if final_dealer_total > 21:
    print('The dealer busts. You win!\n')
    play_again()
  elif final_user_total > final_dealer_total:
    print('You win!\n')
    play_again()
  elif final_dealer_total > final_user_total:
    print('You lose.\n')
    play_again()
  else:
    print('A push is a win.\n')
    play_again()

def play_again():
  play = input('Do you want to play another game? Type \'y\' or \'n\'.')
  if play == 'y':
    clear()
    print(logo)
    play_blackjack()
  else:
    exit()

def play_blackjack():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  # The initial deal
  (user_hand, dealer_hand) = deal(cards)

  # main game play while loop
  play = True
  while play:
    # Calculates the sum of each hand
    print(f"Your hand: {user_hand}")
    print(f"The dealer shows: [{dealer_hand[0]}]\n")
    (user_total, dealer_total) = card_total(user_hand, dealer_hand)

    # Checks for blackjacks
    (player_blackjack, dealer_blackjack) = blackjack(user_total, dealer_total, user_hand, dealer_hand)
    if player_blackjack == True and dealer_blackjack != True:
      print('Winner, winner, chicken dinner!')
      play_again()
    if dealer_blackjack == True and player_blackjack != True:
      print('The house always wins. You lose.')
      play_again()
    if dealer_blackjack == True and player_blackjack == True:
      print('A push is a win.')
      play_again()

    # Is the user's score over 21?
    bust = bust_check(user_hand, user_total)
    if bust == False:
      print('You bust with too many cards. You lose.')
      play_again()
      
    # Ask the user if they want to get another card.
    another_card = input('Hit or stay? Do you want another card? Type \'y\' or \'n\': ')
    if another_card == 'n':
      print('Stay. I also like to live dangerously.\n')
      play = False
      
    else:
      user_hand.append(random.choice(cards))
    # loop to the top of the while loop

  
  # check for soft 17
  if soft_seventeen(dealer_hand, dealer_total) == True:
    dealer_hand.append(random.choice(cards))
  
  # the computer takes cards
  while computer_play(dealer_hand, dealer_total):
    dealer_hand.append(random.choice(cards))
    dealer_total = sum(dealer_hand)

  # calculate the winner
  winner(user_total, dealer_total, user_hand, dealer_hand)


print(logo)
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start == 'y':
  play_blackjack()
