
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


def tens_func(name):
  total = 0
  true_lst = ['t', 'r', 'u', 'e']
  for let in true_lst:
    total += name.lower().count(let)
  return total

def ones_func(name):
  total = 0
  love_lst = ['l', 'o', 'v', 'e']
  for let in love_lst:
    total += name.lower().count(let)
  return total

tens = tens_func(name1)
tens += tens_func(name2)

ones = ones_func(name1)
ones += ones_func(name2)

score_list = [str(tens), str(ones)]
score = ''.join(score_list)


if int(score) < 10 or int(score) > 90:
  print(f'Your score is {score}, you go together like coke and mentos.')
elif int(score) >= 40 and int(score) <= 50:
  print(f'Your score is {score}, you are alright together.')
else: 
  print(f'Your score is {score}.')
