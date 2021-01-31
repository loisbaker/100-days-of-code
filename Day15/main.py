# Day 15: create a coffee machine simulator

import coffee_data


def pay():
    print("Please insert coins.")
    quarters = float(input('How many quarters? '))
    dimes = float(input('How many dimes? '))
    nickels = float(input('How many nickels? '))
    pennies = float(input('How many pennies? '))
    payment = quarters * 0.25 + dimes*0.1 + nickels * 0.05 + pennies * 0.01
    return payment


def check_payment(choice, payment):
    price = coffee_data.menu[choice]['cost']
    if price > payment:
        print('Sorry, that\'s not enough money.')
        return False
    else:
        return True


def check_resources(menu_choice, resources):
    if coffee_data.menu[menu_choice]['ingredients']['water'] > resources['water']:
        print('Sorry, there\'s not enough water')
        return False
    elif coffee_data.menu[menu_choice]['ingredients']['milk'] > resources['milk']:
        print('Sorry, there\'s not enough milk')
        return False
    elif coffee_data.menu[menu_choice]['ingredients']['coffee'] > resources['coffee']:
        print('Sorry, there\'s not enough coffee')
        return False
    else:
        return True


def update_resources(menu_choice, resources, money_amount):
    resources['water'] -= coffee_data.menu[menu_choice]['ingredients']['water']
    resources['milk'] -= coffee_data.menu[menu_choice]['ingredients']['milk']
    resources['coffee'] -= coffee_data.menu[menu_choice]['ingredients']['coffee']
    money_amount += coffee_data.menu[menu_choice]['cost']
    return resources, money_amount


def run_coffee_machine(current_resources, money):
    # Get user choice
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'report':
        print(f"Water: {current_resources['water']}ml\nMilk: {current_resources['milk']}ml\nCoffee: "
              f"{current_resources['coffee']}g\nMoney: ${money}")
    elif choice == 'off':
        return
    else:
        payment = pay()
        enough_payment = check_payment(choice, payment)
        enough_resources = check_resources(choice, current_resources)
        if enough_payment and enough_resources:
            # Give change
            print(f"Here's ${round(payment - coffee_data.menu[choice]['cost'],2)} change")

            # Update resources
            current_resources, money = update_resources(choice, current_resources, money)

            # Give coffee
            print(f"Here's your {choice}, enjoy!")

    run_coffee_machine(current_resources, money)


start_resources = coffee_data.resources.copy()
run_coffee_machine(start_resources, 0)
