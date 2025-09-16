number_juniors = int(input())
number_seniors = int(input())
type_road = str(input())

price_junior = 0
price_seniors = 0
total_price = 0
expenses = 0
total_participants = number_juniors + number_seniors

if type_road == "trail":
    price_junior = 5.50
    price_seniors = 7
    total_price = number_juniors * price_junior + number_seniors * price_seniors
elif type_road == "cross-country":
    price_junior = 8
    price_seniors = 9.50
    total_price = number_juniors * price_junior + number_seniors * price_seniors
    if total_participants >= 50:
        total_price -= total_price * 0.25
elif type_road == "downhill":
    price_junior = 12.25
    price_seniors = 13.75
    total_price = number_juniors * price_junior + number_seniors * price_seniors
elif type_road == "road":
    price_junior = 20
    price_seniors = 21.50
    total_price = number_juniors * price_junior + number_seniors * price_seniors

expenses = total_price * 0.05
print(f"{total_price - expenses:.2f}")


