from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menuitem = MenuItem("name","water","milk","coffee","cost")

coffeemaker = CoffeeMaker()

moneymachine = MoneyMachine()


condition = True
while condition:
    choice = input(f"What do you like {menu.get_items()} :").lower()
    if choice in ["espresso", "latte", "cappuccino"]:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    elif choice == "off":
        condition = False
    else:
        print("Invalid Input")

