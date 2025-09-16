budget = float(input())
price_category = input()
number_of_people = int(input())

ticket_price_vip = 499.99
ticket_price_normal = 249.99

transport = 0
ticket_price = 0

if 1 <= number_of_people <= 4:
    transport = budget * 0.75
    money_left = budget - transport
    if price_category == "Normal":
        ticket_price = number_of_people * ticket_price_normal
    elif price_category == "VIP":
        ticket_price = number_of_people * ticket_price_vip
elif 5 <= number_of_people <= 9:
    transport = budget * 0.60
    money_left = budget - transport
    if price_category == "Normal":
        ticket_price = number_of_people * ticket_price_normal
    elif price_category == "VIP":
        ticket_price = number_of_people * ticket_price_vip
elif 10 <= number_of_people <= 24:
    transport = budget * 0.50
    money_left = budget - transport
    if price_category == "Normal":
        ticket_price = number_of_people * ticket_price_normal
    elif price_category == "VIP":
        ticket_price = number_of_people * ticket_price_vip
elif 25 <= number_of_people <= 49:
    transport = budget * 0.40
    money_left = budget - transport
    if price_category == "Normal":
        ticket_price = number_of_people * ticket_price_normal
    elif price_category == "VIP":
        ticket_price = number_of_people * ticket_price_vip
elif number_of_people >= 50:
    transport = budget * 0.25
    money_left = budget - transport
    if price_category == "Normal":
        ticket_price = number_of_people * ticket_price_normal
    elif price_category == "VIP":
        ticket_price = number_of_people * ticket_price_vip

if money_left > ticket_price:
    print(f"Yes! You have {money_left - ticket_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {ticket_price - money_left:.2f} leva.")