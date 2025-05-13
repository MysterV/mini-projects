from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
kofi = CoffeeMaker()
moni = MoneyMachine()
while True:
    choice = input(f'What do you want? {menu.get_items()[:-1]}: ')
    if choice == 'off':
        break
    elif choice == 'report':
        kofi.report()
        moni.report()

    elif coffee := menu.find_drink(choice):
        if kofi.is_resource_sufficient(coffee):
            if moni.make_payment(coffee.cost):
                kofi.make_coffee(coffee)
