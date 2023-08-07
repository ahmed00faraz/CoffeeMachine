MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

Machine_money = 0


def suff_money(drink, total_money):
    return total_money >= MENU[drink]["cost"]


def check(drink):
    """checks if resources are sufficient """
    ret = ""
    req = MENU[drink]["ingredients"]
    water = req["water"] <= resources["water"]
    milk = req["milk"] <= resources["milk"]
    coffee = req["coffee"] <= resources["coffee"]
    if milk and water and coffee:
        resources["water"] -= req["water"]
        resources["milk"] -= req["milk"]
        resources["coffee"] -= req["coffee"]
        return "suff"
    else:
        if not water:
            ret += "water"
        if not milk:
            ret += " milk"
        if not coffee:
            ret += "coffee"
        ret = ", ".join(ret.split(" "))
        return "Sorry there is not enough " + ret


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print(f'Water : {resources["water"]}ml')
        print(f'Milk : {resources["milk"]}ml')
        print(f'coffee : {resources["coffee"]}g')
        print(f'Money : ${Machine_money}')
    elif choice == "latte" or choice == "cappuccino" or choice == "espresso":
        print("Please insert coins")
        quarters = int(input("How many Quarters? : "))
        dimes = int(input("How many dimes? : "))
        nickles = int(input("How many nickles? : "))
        pennies = int(input("How many pennies? : "))
        total_mon = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        if not suff_money(choice, total_mon):
            print("Sorry that's not enough money. Money refunded.")
            continue
        elif not check(choice) == "suff":
            print(check(choice))
            continue
        else:
            Machine_money += MENU[choice]["cost"]
            change = total_mon - MENU[choice]["cost"]
            print(f"Here is ${round(change, 2)} in change.")
            print(f"Here is your {choice} ☕️. Enjoy!")
    else:
        print("Invalid input")
