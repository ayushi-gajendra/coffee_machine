profit=0.0

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
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

def check_resources(drink):
    items=""
# to check if there are enough resources to make the resp drink
    for items in MENU[drink]["ingredients"]:
        if resources[items]<=MENU[drink]["ingredients"][items]:
            print(f"Sorry there is not enough {items}")
            return False
    return True

def calculate_change(cost_of_drink):
    print("Please insert coins: ")
    q= float(input("how many quarters?:"))
    d = float(input("how many dimes?:"))
    n = float(input("how many nickles?:"))
    p = float(input("how many pennies?:"))

    total= (q*0.25) + (d*0.10) + (n*0.05) +(p*0.01)
    change = round((total - cost_of_drink),2)

    if total < cost_of_drink:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${change}in change.")
        return True


def make_coffee(drink):
    # we have to subtract amount of ingredients used in the drink from the resources
    # add the cost of drink to profit
    #take money, calculate change

    global profit
    resources_sufficient = False
    resources_sufficient = check_resources(drink)
    if resources_sufficient:
        coffee_made = calculate_change(MENU[drink]["cost"])
        if coffee_made:
            for items in MENU[drink]["ingredients"]:
                resources[items]-= MENU[drink]["ingredients"][items]
            profit += MENU[drink]["cost"]
            print(f"Here is your {drink} ☕️. Enjoy!")


is_on=True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g")
        print(f"Money:{profit}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        make_coffee(choice)
    else:
        print("Wrong input. Please re-enter your choice")
