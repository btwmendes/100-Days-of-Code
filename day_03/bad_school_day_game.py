print(r'''

    \_/
  --(_)--  .
    / \   /_\
          |Q|
    .-----' '-----.                                  __
   /____[SCHOOL]___\                                ()))
    | [] .-.-. [] |                                (((())
  ..|____|_|_|____|..................................)(... ldb

''')
import time
time.sleep(3)
print()
print()
print('Welcome to Bad School Day\n\n')
time.sleep(3)

print('''
  ( ) ( )    
    `_^_'    
    / |,\         
   |- ' -|       
    \_,_/       
    /___\ 

''')
print('BUZZ...BUZZ...BUZZ.\nYour alarm is telling you to wake up for school')
alarm = input('Do I want to wake up now or hit the snooze? Type wake or snooze: ')
if alarm.lower() == 'snooze':
    snooze = True
    for num in range(10, -1, -1):
        print(f'{num} more minutes to sleep in.')
        time.sleep(1)
    print('''
  ( ) ( )    
    `_^_'    
    / |,\         
   |- ' -|       
    \_,_/       
    /___\ 

''')
    print("It is time to wake up.")
else:
    snooze = False

homework = input('I guess I didn\'t finish that math homework last night. It should only take a minute. Want to finish it now? Type Y or N. ')
shower = input("Do I want to shower? Type Y or N.  ")
breakfast = input("Am I going to eat breakfast? Type Y or N. ")
print()

print('That was a busy morning. Time to catch the bus.')
print('''
  ___________________
   |,-----.,-----.,---.\
   ||     ||     ||    \\
   |`-----'|-----||-----\`----.
   [       |    -||-   _|    (|
   [  ,--. |_____||___/.--.   |
   =-(( `))-----------(( `))-==
  jrei`--'             `--'
  ''')
print()

if snooze == True or homework.upper() == 'Y' or shower.upper() == 'Y' or breakfast.upper() =='Y':
    bus = 'N'
    print('AGHHH! The bus left me! I\'m not even late! I hate this bus! I hate the whole world!\n')
    walk = input('Should I walk or ride my bike? Type walk or bike: ').lower()
    print()
    if walk == 'bike':
        print('My bike tire is flat and I don\'t know how to fix it. Time to walk 2 miles to school. I like walking anyway. 2 miles won\'t take me that long. I\'ll play games on my phone to pass the time.\n')
    else:
        print('I like walking anyway. 2 miles won\'t take me that long. I\'ll play games on my phone to pass the time.\n')

    time.sleep(2)
    print('''
         (   )
  (   ) (
   ) _   )
    ( \_
  _(_\ \)__
 (____\___))
    ''')
    time.sleep(2)
    print('Are you kidding me! I just stepped in dog poo! Who doesn\'t pick up their dog\'s poo! AARRGGH!\n')
else:
    print('Good news - I made it onto the bus. Bad news - I sat in a wet puddle on the seat. What is that smell?\n')
    bus = 'Y'
    print()

print('I\'m finally at school. Just need to open my locker. Hmm what\'s the combo again?\n')

# Guess the number mini game
import random
secretNumber = random.randint(1,100)
print('Guess a number between 1 and 100. You have 6 guesses.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess.

if guess == secretNumber:
    print(f'Good job! You guessed the number in {guessesTaken} tries.')
else:
    print(f'Nope. The combo is {secretNumber}.')
    diff = abs(secretNumber - guess)
    print(f'You were {diff} away from the combination. Game Over :P')
    from sys import exit
    exit()

print()
print('Wow...there\'s my crush. Now\'s the time to get a date to the school dance.\n')
date = input('Should I ask my crush to the dance? Type Y or N: ').upper()
if date == 'Y' and bus == 'Y':
    print("You crush says, 'Oh hi...what is that smell? What\'s that stain on your pants. I would never go on a date with someone that smells like that!")
elif date == 'Y' and (walk == 'walk' or walk == 'bike'):
    print("You crush says, 'Oh hi...what is that smell? It smells like dog poo. I would never go on a date with someone that smells like that!")
else:
    print('You\'re a chicken. Game Over.')

# print()
# print('Oh no! You woke up late for school again')
