#!/usr/bin/env python3

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random
num = random.randint(0, len(names) -1 )

print(f'{names[num]} is going to buy the meal today!')
