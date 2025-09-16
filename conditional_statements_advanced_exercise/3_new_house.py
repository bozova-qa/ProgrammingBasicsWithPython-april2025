type_of_flowers = input()
number_flowers = int(input())
budget = int(input())

total_price = 0

price_roses = 5.00
price_dahlia = 3.80
price_tulip = 2.80
price_narcissus = 3
price_gladiolus = 2.50

if type_of_flowers == "Roses":
    if number_flowers > 80:
        discount = (number_flowers * price_roses) * 0.1
        total_price += number_flowers * price_roses - discount
    elif number_flowers <= 80:
        total_price += number_flowers * price_roses
elif type_of_flowers == "Dahlias":
    if number_flowers > 90:
        discount = (number_flowers * price_dahlia) * 0.15
        total_price += number_flowers * price_dahlia - discount
    elif number_flowers <= 90:
        total_price += number_flowers * price_dahlia
elif type_of_flowers == "Tulips":
    if number_flowers > 80:
        discount = (number_flowers * price_tulip) * 0.15
        total_price += number_flowers * price_tulip - discount
    elif number_flowers <= 80:
        total_price += number_flowers * price_tulip
elif type_of_flowers == "Narcissus":
    if number_flowers < 120:
        total_price += number_flowers * (price_narcissus + price_narcissus * 0.15)
    elif number_flowers >= 120:
        total_price += number_flowers * price_narcissus
elif type_of_flowers == "Gladiolus":
    if number_flowers < 80:
        total_price += number_flowers * (price_gladiolus + price_gladiolus * 0.20)
    elif number_flowers >= 80:
        total_price += number_flowers * price_gladiolus

if budget >= total_price:
    print(f"Hey, you have a great garden with {number_flowers} {type_of_flowers} and {budget - total_price:.2f} leva left.")
elif budget < total_price:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
