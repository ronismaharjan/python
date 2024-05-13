from machine_data import resources, MENU

# Function to display the availabe resources


def show_report():
    """This function shows the current data of the machine """

    print(
        f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')

# Function to compare the resources form machine and from the drinks


def compare_resources(machine_resources, coffee_resources):
    """Takes the ingredient of the given drink and machine and check if there is enough resources to create a drink or not"""
    not_enough_ingredients = []
    enough_amount = 0
    for ingredient in coffee_resources:
        if machine_resources[ingredient] >= coffee_resources[ingredient]:
            enough_amount += 1
        else:
            not_enough_ingredients.append(ingredient)
    if enough_amount == len(coffee_resources):
        return True
    else:
        return not_enough_ingredients
# Function to add all types of coin into one total dollor


def coin_adder(num_of_quaters_coin, num_of_dimes_coin, num_of_pennies_coin, num_of_nickles_coin):
    """Takes all the coin and add it to simple decimal value"""
    total_quaters = num_of_quaters_coin * 0.25
    total_dimes = num_of_dimes_coin * 0.10
    total_pennies = num_of_pennies_coin * 0.01
    total_nickles = num_of_nickles_coin * 0.05
    total_dollers = total_quaters + total_dimes + total_pennies + total_nickles
    return round(total_dollers, 2)

# Function to update the dictionary value of the machine


def update_inventory(ingredients, money):

    for ingre in ingredients:
        resources[ingre] -= ingredients[ingre]
    resources["money"] += money


# Turn off the coffee Machine By entering 'off' to the prompt
is_on = True
resources["money"] = 0
while is_on:
    # Prompt user what they want
    user_choice = input(
        "What would you like? (espresso/latte/cappuccino: ").lower()
    if user_choice == "off":
        is_on = False
    # Print the report
    elif user_choice == "report":
        show_report()
    elif user_choice in MENU:
        # Checking resources is sufficient or not
        enough_resources = compare_resources(
            resources, MENU[user_choice]["ingredients"])
        if enough_resources == True:
            drink_cost = MENU[user_choice]['cost']

            # process coin ask user to put coins
            quaters = int(input("Enter the money in quaters: "))
            dimes = int(input("Enter the money in dimes: "))
            nickles = int(input("Enter the money in nickles: "))
            pennies = int(input("Enter the money in pennies: "))
            total_user_coin = coin_adder(quaters, dimes, nickles, pennies)

            # Checking the transaction is successfull or not
            if total_user_coin >= drink_cost:

                remaining_exchange = round((total_user_coin - drink_cost), 2)

                if remaining_exchange > 0:
                    print(f"Here is your exchange {remaining_exchange}")
                # Making the coffee
                print(f"Enjoy your {user_choice}")

                # Updating the inventory
                update_inventory(MENU[user_choice]
                                 ["ingredients"], drink_cost)

            else:
                print(
                    f"you have put ${total_user_coin} but {user_choice} cost ${drink_cost}")

        else:
            print(f"There is not enough {' '.join(enough_resources)}")
            is_on = False

    else:
        print("You have typed out of context.")
