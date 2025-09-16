group_budget = int(input())
season = str(input())
number_fisherman = int(input())

total_price = 0

boat_rent_spring = 3000
boat_rent_summer_autumn = 4200
boat_rent_winter = 2600

if season == "Spring":
    if number_fisherman <= 6:
        discount = boat_rent_spring * 0.1
        total_price = boat_rent_spring - discount
    elif 7 <= number_fisherman <= 11:
        discount = boat_rent_spring * 0.15
        total_price = boat_rent_spring - discount
    elif number_fisherman >= 12:
        discount = boat_rent_spring * 0.25
        total_price = boat_rent_spring - discount
elif season == "Summer" or season == "Autumn":
    if number_fisherman <= 6:
        discount = boat_rent_summer_autumn * 0.1
        total_price = boat_rent_summer_autumn - discount
    elif 7 <= number_fisherman <= 11:
        discount = boat_rent_summer_autumn * 0.15
        total_price = boat_rent_summer_autumn - discount
    elif number_fisherman >= 12:
        discount = boat_rent_summer_autumn * 0.25
        total_price = boat_rent_summer_autumn - discount
elif season == "Winter":
    if number_fisherman <= 6:
        discount = boat_rent_winter * 0.1
        total_price = boat_rent_winter - discount
    elif 7 <= number_fisherman <= 11:
        discount = boat_rent_winter * 0.15
        total_price = boat_rent_winter - discount
    elif number_fisherman >= 12:
        discount = boat_rent_winter * 0.25
        total_price = boat_rent_winter - discount

if number_fisherman % 2 == 0 and season != "Autumn":
    discount = total_price * 0.05
    total_price -= discount

if group_budget >= total_price:
    print(f"Yes! You have {group_budget - total_price:.2f} leva left.")
elif group_budget < total_price:
    print(f"Not enough money! You need {total_price - group_budget:.2f} leva.")
