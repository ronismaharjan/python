from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True
while is_on:
    menu = Menu()
    user_choice = input(f"Which drink do you want ({menu.get_items()}): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        try:
            drink = menu.find_drink(user_choice)
            if coffee_maker.is_resource_sufficient(drink) and menu.find_drink(user_choice):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        except:
            print("There occurs an error..")
