money_needed = float(input())
money_available = float(input())

total_days = 0
consecutive_days_spending = 0

while consecutive_days_spending < 5:
    total_days += 1
    type_of_action = input()
    money = float(input())

    if type_of_action == "spend":
        consecutive_days_spending += 1
        money_available -= money
        if money_available < 0:
            money_available = 0
    elif type_of_action == "save":
        consecutive_days_spending = 0 # reset because he broke the streak
        money_available += money

    if money_available >= money_needed:
        print(f"You saved the money for {total_days} days.")
        break

if consecutive_days_spending >= 5:
    print("You can't save the money.")
    print(total_days)

###

money_needed = float(input())
available_money = float(input())

counter_spend = 0
days_counter = 0
saved_money = 0

while True:
    action = str(input())
    days_counter += 1
    if action == "save":
        money = float(input())
        saved_money += money
    elif action == "spend":
        money = float(input())
        available_money -= money
        if available_money < 0:
            available_money = 0
        counter_spend += 1
        if counter_spend == 5:
            print("You can't save the money.")
            print(f"{days_counter}")
            break

    total_money = saved_money + available_money

    if total_money >= money_needed:
        print(f"You saved the money for {days_counter} days.")
        break