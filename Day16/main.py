from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()

continue_coffee = True
while continue_coffee:
    choice = input(f"What would you like? ({my_menu.get_items()}): ").lower()
    if choice == 'report':
        my_coffee_maker.report()
        my_money_machine.report()
    elif choice == 'off':
        continue_coffee = False
    else:
        my_menu_item = my_menu.find_drink(choice)
        if my_menu_item is not None:
            is_sufficient_resource = my_coffee_maker.is_resource_sufficient(my_menu_item)
            if is_sufficient_resource:
                is_sufficient_payment = my_money_machine.make_payment(my_menu_item.cost)
                if is_sufficient_payment:
                    my_coffee_maker.make_coffee(my_menu_item)
