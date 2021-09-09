MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def report():
    print(f"""
Water: {resources["water"]}mL
Milk: {resources["milk"]}mL
Coffee: {resources["coffee"]}g
Money: ${resources["money"]}
    """)


def end_program():
    return


def check_resources(order_ingedients):
    go_time = True
    for item in order_ingedients:
        if resources[item] < order_ingedients[item]:
            print(f'Sorry there is not enough {item}.')
            go_time = False
    return go_time


def calculate_coins(quarter, dime, nickel, penny):
    total = 0
    total += (quarter * 0.25)
    total += (dime * 0.1 )
    total += (nickel * 0.05)
    total +=  (penny * 0.01)
    return total

machine_is_on = True
while machine_is_on:
    coffee_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_order == 'report':
        report()
        continue
    elif coffee_order == 'off':
        exit()

    drink = MENU[coffee_order]
    enough_supplies = check_resources(drink['ingredients'])
    if enough_supplies == False:
        continue

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    sum_coins = round(calculate_coins(quarters, dimes, nickels, pennies), 2)

    if sum_coins < MENU[coffee_order]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        continue
    else:
        # opportunity to use a for loop to tighten up the code
        resources['water'] = resources['water'] - MENU[coffee_order]['ingredients']['water']
        resources['milk'] = resources['milk'] - MENU[coffee_order]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - MENU[coffee_order]['ingredients']['coffee']
        resources['money'] =  resources['money'] + float(MENU[coffee_order]['cost'])
        if sum_coins > MENU[coffee_order]['cost']:
            refund = round(sum_coins - MENU[coffee_order]['cost'], 2)
            print(f"Here is ${refund} in change.")
            print(f"Here is your {coffee_order} ☕. Enjoy!")





