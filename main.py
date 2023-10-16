from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


maker = CoffeeMaker()
money = MoneyMachine()
item = Menu()

while(True):
    ans = input(f"What would you like ? {item.get_items()}:")
    if(ans == "off"):
        break
    elif (ans == "report"):
        maker.report()
        money.report()

    else:
        if not maker.is_resource_sufficient(item.find_drink(ans)):
            break
        if not money.make_payment(item.find_drink(ans).cost):
            break

        maker.make_coffee(item.find_drink(ans))
