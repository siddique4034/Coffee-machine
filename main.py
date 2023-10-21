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


def check_ingredients(customer_order):
	if (MENU[customer_order]["ingredients"]["water"] > resources["water"]) or (MENU[customer_order]["ingredients"]["milk"] > resources["milk"]) or (MENU[customer_order]["ingredients"]["coffee"] > resources["coffee"]) :
		return False
	else:
		return True


def process_coins():
	quanters = int(input("Please insert coins (only quanters): "))
	dimes = int(input("Please insert coins (only dimes): "))
	nickles = int(input("Please insert coins (only nickles): "))
	pennies = int(input("Please insert coins (only pennies): "))
	total_coins = quanters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
	return total_coins


def transaction(total_coins, resources):
	global money
	if total_coins < MENU[user_prompt]["cost"]: 
		print(f"Sorry that's not enough money for {user_prompt}. Money refunded.")
	elif total_coins >= MENU[user_prompt]["cost"]:
		print(f"Here is your {user_prompt} . Your change is {(total_coins - MENU[user_prompt]['cost']):.2f}.")
		for item in resources:
			resources[item] = resources[item] - MENU[user_prompt]["ingredients"][item]
		money += MENU[user_prompt]["cost"]


def report():
	print(f"Water: {resources['water']}ml"
				f"\nMilk: {resources['milk']}ml"
				f"\nCoffee: {resources['coffee']}g."
				f"\nMoney: ${money:.2f}")



serve_next_customer = True
ingredients_sufficient = True
money = 0

while serve_next_customer:
	user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
	if user_prompt == "off":
		serve_next_customer =  False
	elif user_prompt == "report":
		report()

	else:
		ingredients_sufficient = check_ingredients(user_prompt)
		if ingredients_sufficient == False:
			print(f"Sorry there is not enough {user_prompt}.")
		else:
			total_coins = process_coins()
			transaction(total_coins, resources)

