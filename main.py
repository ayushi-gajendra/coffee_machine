# ---------------------- Initial Setup ---------------------- #
profit = 0.0  # Tracks total money earned

# Menu of available drinks with ingredients and cost
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

# Available resources in the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# ---------------------- Resource Check ---------------------- #
def check_resources(drink):
    """Checks if enough ingredients are available for the selected drink."""
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# ---------------------- Payment Calculation ---------------------- #
def calculate_change(cost_of_drink):
    """Calculates if the user has inserted enough money and returns change if any."""
    print("Please insert coins: ")
    q = float(input("How many quarters?: "))
    d = float(input("How many dimes?: "))
    n = float(input("How many nickles?: "))
    p = float(input("How many pennies?: "))

    total = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    change = round((total - cost_of_drink), 2)

    if total < cost_of_drink:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${change} in change.")
        return True

# ---------------------- Make Coffee ---------------------- #
def make_coffee(drink):
    """Deducts used ingredients, updates profit, and serves the drink."""
    global profit
    if check_resources(drink):
        if calculate_change(MENU[drink]["cost"]):
            for item in MENU[drink]["ingredients"]:
                resources[item] -= MENU[drink]["ingredients"][item]
            profit += MENU[drink]["cost"]
            print(f"Here is your {drink} ☕️. Enjoy!")

# ---------------------- Main Loop ---------------------- #
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice in MENU:
        make_coffee(choice)
    else:
        print("Wrong input. Please re-enter your choice.")
