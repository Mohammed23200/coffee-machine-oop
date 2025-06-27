from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu1 = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    options = menu1.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        print("See you later! 👋")
        is_on = False
    elif choice == "report":
        print("Coffee Maker Report:")
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu1.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            boole1=money_machine.make_payment(drink.cost)
            if boole1:
                coffee_maker.make_coffee(drink)
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources.")