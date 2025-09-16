total_stay = int(input())
type_accommodation = str(input())
feedback = str(input())

total_price = 0
nights = total_stay - 1

price_room_for_one_person = 18.00
price_for_apartment = 25.00
price_for_president_apartment = 35.00

if type_accommodation == "room for one person":
    total_price += nights * price_room_for_one_person
elif type_accommodation == "apartment":
    if total_stay < 10:
        total_price += nights * price_for_apartment
        total_price -= total_price * 0.30
    elif 10 <= total_stay <= 15:
        total_price += nights * price_for_apartment
        total_price -= total_price * 0.35
    elif total_stay > 15:
        total_price += nights * price_for_apartment
        total_price -= total_price * 0.50
elif type_accommodation == "president apartment":
    if total_stay < 10:
        total_price += nights * price_for_president_apartment
        total_price -= total_price * 0.10
    elif 10 <= total_stay <= 15:
        total_price += nights * price_for_president_apartment
        total_price -= total_price * 0.15
    elif total_stay > 15:
        total_price += nights * price_for_president_apartment
        total_price -= total_price * 0.20

if feedback == "positive":
    total_price += total_price * 0.25
elif feedback == "negative":
    total_price -= total_price * 0.10

print(f"{total_price:.2f}")
