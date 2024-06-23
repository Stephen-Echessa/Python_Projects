from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

should_continue = True

coffee_maker = CoffeeMaker()
coin_processor = MoneyMachine()
menu = Menu()

while should_continue:
    # Input what customer would like
    flavour = input(f"What would you like? ({menu.get_items()})")

    if flavour == "off":
        should_continue = False

    #Print report of resources
    elif flavour == "report":
        coffee_maker.report()
        coin_processor.report()

    else:
        # Check if input is in the menu
        chosen_flavour = menu.find_drink(flavour)

        # Check if resources sufficient
        if coffee_maker.is_resource_sufficient(chosen_flavour):
            # Process coins
            if coin_processor.make_payment(chosen_flavour.cost):
                # Make coffee
                coffee_maker.make_coffee(chosen_flavour)

