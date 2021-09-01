#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print('Welcome to the tip calculator.')
print('What was the total bill?')
total = input('$')

print('What percentage tip would you like to give? Type the number without the percent sign, i.e. 10, 15, 25, etc.')
percent = input()

print('How many people are splitting the bill?')
people = input()

tip = (float(total) / int(people)) * (1 + (int(percent)/100))
rounded_tip = round(tip, 2)
final_amt = "{:.2f}".format(rounded_tip)
print(f'Each person should pay {final_amt}.')