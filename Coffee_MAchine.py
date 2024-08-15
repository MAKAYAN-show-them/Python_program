MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}

resources = {
    "water":300,
    "milk":200,
    "coffee":100,
}


coins = { 
    "quarters": {
        "value" : 0.25,
        "coins_inserted": 0
    },
    "dimes" : {
        "value" : 0.10,
         "coins_inserted": 0
    },
    "nickles" : {
        "value": 0.05,
        "coins_inserted": 0
    },
    "pennies" : {
        "value": 0.01,
        "coins_inserted":0
    }
}


def asking_user():
    ''' Prompt user by asking “
 What would you like? (espresso/latte/cappuccino):​ ” 
a. Check the user’s input to decide what to do next.  
b. The prompt should show every time action has completed, e.g. once the drink is 
dispensed. The prompt should show again to serve the next customer. 
    '''
    wrong_input = True
    while wrong_input:
        user_choice = input("What would you like? (espresso/latte/cappuccino) :").lower()
        if user_choice in ["espresso","latte","cappuccino","off","report"]:
            wrong_input = False
            return user_choice
        else:
            wrong_input = True


def checking_resources(choosed_coffee):
    selected_coffee = MENU[choosed_coffee]["ingredients"]
    for ingredient,quantity_left in selected_coffee.items():
        if resources[ingredient] - selected_coffee[ingredient]  < 0:
            print(f"Sorry there is not enough {ingredient}")
            return False
    else:
        return True



def insert_coins():
    number_range = [number for number in range(0,101)]
    Total_value = 0
    for coin,value in coins.items():
        wrong_input = True
        while wrong_input:
            total_coin_inserted = int(input(f"please insert the {coin}:.Remeber you can't insert more than 100 {coin}: "))
            if total_coin_inserted in number_range:
                wrong_input = False
                coins[coin]["coins_inserted"] = coins[coin]["coins_inserted"] + total_coin_inserted
                total_inserted_coin_value = coins[coin]["value"] * total_coin_inserted
                Total_value += total_inserted_coin_value
            else:
                print("Inserts the coin Properly")
                wrong_input = True

    return Total_value
    

def returning_coins_to_user(coin, returning_coins):
    coins[coin]["coins_inserted"] -= returning_coins
    print(f"Here is your change: {returning_coins} {coin}(s)")
    return coins[coin]["value"] * returning_coins


def refunding_amount_saving_profit(selected_coffee, Total_value_coins_inserted):
    if MENU[selected_coffee]["cost"] < Total_value_coins_inserted:
        refund_amount = Total_value_coins_inserted - MENU[selected_coffee]["cost"]

        for coin, value in coins.items():
            if refund_amount <= 0:
                break
            
            returning_coins = refund_amount // coins[coin]["value"]
            coins_available_machine = coins[coin]["coins_inserted"]
            
            if coins_available_machine < returning_coins:
                refund_amount -= returning_coins_to_user(coin=coin, returning_coins=coins_available_machine)
            else:
                refund_amount -= returning_coins_to_user(coin=coin, returning_coins=returning_coins)
        
        if refund_amount > 0:
            print("Sorry, the machine doesn't have enough coins to give you exact change.")
        else:
            decreasing_quantity(choosed_coffee=selected_coffee)

    else:
        print("Sorry, that's not enough money. Money refunded.")


# Example dictionary structures for coins and MENU
coins = {
    "quarters": {"value": 0.25, "coins_inserted": 10},
    "dimes": {"value": 0.10, "coins_inserted": 10},
    "nickels": {"value": 0.05, "coins_inserted": 10},
    "pennies": {"value": 0.01, "coins_inserted": 10}
}

MENU = {
    "latte": {"cost": 2.5},
    "espresso": {"cost": 1.5},
    "cappuccino": {"cost": 3.0}
}

def decreasing_quantity(choosed_coffee):
    print(f"Serving {choosed_coffee}. Inventory updated.")

    

def decreasing_quantity(choosed_coffee):
    selected_coffee = MENU[choosed_coffee]["ingredients"]
    for ingredient,quantity_left in selected_coffee.items():
        resources[ingredient] = resources[ingredient] - selected_coffee[ingredient]

def report():
    print(f"Water :{resources['water']}ml")
    print(f"Milk :{resources['milk']}ml")
    print(f"Coffee :{resources['coffee']}g")
    Total_profit = 0

    for coin in coins:
        Total_profit += coins[coin]["value"] * coins[coin]["coins_inserted"]

    print(f"Total Profit: ${Total_profit}")



def checking_user_input():
    '''classifying Task on the basics of user Input'''

    user_input = asking_user()
    if user_input in ["espresso","latte","cappuccino"]:
        continue_operation = checking_resources(user_input)
        if continue_operation == True :
            inserting_coins = insert_coins()
            refunding_amount_saving_profit(user_input,inserting_coins)
            print(f"Here is your {user_input}")
            return True , True
        else:
            return False , True
    elif user_input == "off":
        return False , False
    
    elif user_input == "report":
        report()
        return True , True
        


machine_running = True
while machine_running:
    machine_reset= True
    while machine_reset:
        machine_reset, machine_running = checking_user_input()

