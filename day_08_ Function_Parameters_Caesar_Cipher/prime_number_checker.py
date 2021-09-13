

def prime_checker(number):
  divisors = []
  for i in range(1, number + 1):
    if number % i == 0:
      divisors.append(i)
  if len(divisors) > 2:
    print('It\'s not a prime number.')
  else:
    print('It\'s a prime number.')

n = int(input("Check this number: "))
prime_checker(number=n)
