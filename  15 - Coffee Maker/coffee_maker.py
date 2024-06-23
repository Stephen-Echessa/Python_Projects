from recipes import MENU
from recipes import resources

# Process coins
def process_coins():
    print("Please insert coins. ")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    return total

should_continue = True

while should_continue:
    def coffee_maker(money):
        #Initialize flavor and money gained
        flavor = input("What would you like? (espresso/latte/cappuccino): ")
        resources_total = money

        # Print report
        if flavor=="report":
            for key in resources:
                print(f"{key.capitalize()}: {resources[key]}")

            
            print(f"Money: ${resources_total}")

        elif flavor=="off":
            return False

        # Check resources if sufficient
        else:

            for ingredient in MENU[flavor]['ingredients']:
                if resources[ingredient] < MENU[flavor]['ingredients'][ingredient] :
                    print(f"Sorry there is not enough {ingredient}")
                    coffee_maker(resources_total)
            
            total = round(process_coins(),1)

            if total < MENU[flavor]["cost"]:
                print(f"Money paid was ${total}")
                print("Sorry that's not enough money. Money refunded")


            else:
                print(f"You have paid {total}")
                change = total - MENU[flavor]["cost"]
                resources_total += MENU[flavor]["cost"]
                print(f"Here is ${round(change,1)} in change")

                for key in resources:
                    resources[key] -= MENU[flavor]["ingredients"][key]

        coffee_maker(resources_total)
            

    should_continue = coffee_maker(0)