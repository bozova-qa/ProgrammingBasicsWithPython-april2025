type_of_fuel = str(input())
liters_fuel = float(input())
club_card = str(input())

total_price = 0

if type_of_fuel == "Gasoline":
    if club_card == "Yes":
        total_price += liters_fuel * (2.22 - 0.18)
    if club_card == "No":
        total_price += liters_fuel * 2.22
elif type_of_fuel == "Diesel":
    if club_card == "Yes":
        total_price = liters_fuel * 2.33
        total_price -= liters_fuel * 0.12
    if club_card == "No":
        total_price = liters_fuel * 2.33
elif type_of_fuel == "Gas":
    if club_card == "Yes":
        total_price = liters_fuel * 0.93
        total_price -= liters_fuel * 0.08
    if club_card == "No":
        total_price = liters_fuel * 0.93

if 20 <= liters_fuel <= 25:
    total_price -= total_price * 0.08
elif liters_fuel > 25:
    total_price -= total_price * 0.1

print(f"{total_price:.2f} lv.")