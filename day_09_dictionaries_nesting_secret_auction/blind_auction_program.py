from replit import clear

from art import logo
print(logo)
print('Welcome to the secret auction program.')

def find_highest_bidder(bidding_record):
  winning_name = ''
  winning_bid = 0
  for name in bidding_record:
    bid_amt = bidding_record[name]
    if bid_amt > winning_bid:
      winning_bid = bid_amt
      winning_name = name
  print(f'The winner is {winning_name} with a bid of ${winning_bid}.')

bid_dict = {}
active_bidders = True
while active_bidders:
  name = input('What is your name?: ').title()
  bid = int(input('What is your bid?: '))
  other_bidders = input('Are there any other bidders? Type \'yes\' or \'no\'.\n').lower()
  bid_dict[name] = bid
 
  if other_bidders == 'no':
    active_bidders = False
    clear()
    find_highest_bidder(bid_dict)
  else:
    clear()
