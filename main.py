from data import MENU, resources

def money(drink,type):
    while True:
        try:
            quarters = int(input("insert quarters: "))
            dimes = int(input("Insert dimes: "))
            nickles = int(input("Insert nickles: "))
            pennies = int(input("Insert pennies: "))
            break
        except:
            print("you need to use numbers")
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total >= drink:
        if total == drink:
            print(f"here is your {type}")
        else:
            print(f"Here is your change: {total - drink}")
        return True
    else:
        print(f"Not enough money, you still miss {round(abs(total - drink), 2)} ")


def make_coffee(water, coffee, cost, type, milk=0):
    if water > resources['water']:
        print("insufficient water")
        return
    elif milk > resources['milk'] and milk > 0:
        print("Insufficent milk")
        return
    elif coffee > resources['coffee']:
        print("Insufficient coffee")
        return
    can_buy = money(cost,type)
    if can_buy:
        resources['water'] -= MENU[type]["ingredients"]["water"]
        if type != "espresso":
            resources['milk'] -= MENU[type]["ingredients"]["milk"]
        resources['coffee'] -= MENU[type]["ingredients"]['coffee']
        resources['money'] += MENU[type]["cost"]


def main():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            print("The machine will turn off now!")
            return False
        elif choice == "report":
            print(resources)
        elif choice == "espresso":
            make_coffee(MENU['espresso']["ingredients"]["water"], MENU['espresso']["ingredients"]['coffee'], MENU['espresso']["cost"],"espresso")
        elif choice == "latte":
            make_coffee(200, 24, 2.5, "latte")
        elif choice == "cappuccino":
            make_coffee(250, 24, 3.0, "cappuccino", 100)
        else:
            print("I did not understand could you say it again please?")


if __name__ == '__main__':
    resources['money'] = 0
    main()