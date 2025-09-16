number_chrysanthemums = int(input())
number_roses = int(input())
number_tulips = int(input())
season = str(input())
holiday = input()

total_price_flowers = 0
price_chrysanthemums = 0
price_roses = 0
price_tulips = 0
price_bouquet = 0
price_arrangement = 2
total_flowers = number_chrysanthemums + number_roses + number_tulips

if season == "Spring":
    price_chrysanthemums = 2.00
    price_roses = 4.10
    price_tulips = 2.50
    price_bouquet = (number_chrysanthemums * price_chrysanthemums + number_roses * price_roses + number_tulips *
                     price_tulips)
    if holiday == "Y":
        price_bouquet += price_bouquet * 0.15
        if number_tulips > 7:
            price_bouquet -= price_bouquet * 0.05
        if total_flowers > 20:
            price_bouquet -= price_bouquet * 0.20
    elif holiday == "N":
        price_bouquet = (number_chrysanthemums * price_chrysanthemums + number_roses * price_roses + number_tulips *
                         price_tulips)
        if number_tulips > 7:
            price_bouquet -= price_bouquet * 0.05
        if total_flowers > 20:
            price_bouquet -= price_bouquet * 0.20

elif season == "Summer":
    price_chrysanthemums = 2.00
    price_roses = 4.10
    price_tulips = 2.50
    price_bouquet = (number_chrysanthemums * price_chrysanthemums + number_roses * price_roses + number_tulips *
                     price_tulips)
    if holiday == "Y":
        price_bouquet += price_bouquet * 0.15
        if total_flowers > 20:
            price_bouquet -= price_bouquet * 0.20
    elif holiday == "N":
        price_bouquet = (number_chrysanthemums * price_chrysanthemums + number_roses * price_roses + number_tulips *
                         price_tulips)
        if total_flowers > 20:
            price_bouquet -= price_bouquet * 0.20

elif season == "Autumn":
    price_chrysanthemums = 3.75
    price_roses = 4.50
    price_tulips = 4.15
    price_bouquet = (number_chrysanthemums * price_chrysanthemums + number_roses * price_roses + number_tulips *
                     price_tulips)
    if holiday == "Y":
        price_bouquet += price_bouquet * 0.15
        if total_flowers > 20:
            price_bouquet -= price_bouquet * 0.20
    elif holiday == "N":
        price_bouquet = (number_chrysanthemums * price_chrysanthemums + number_roses * price_roses + number_tulips *
                         price_tulips)
        if total_flowers > 20:
            price_bouquet -= price_bouquet * 0.20

elif season == "Winter":
    price_chrysanthemums = 3.75
    price_roses = 4.50
    price_tulips = 4.15
    price_bouquet = (number_chrysanthemums * price_chrysanthemums + number_roses * price_roses + number_tulips *
                     price_tulips)
    if holiday == "Y":
        price_bouquet += price_bouquet * 0.15
        if number_roses >= 10:
            price_bouquet -= price_bouquet * 0.10
        if total_flowers > 20:
            price_bouquet -= price_bouquet * 0.20
    elif holiday == "N":
        price_bouquet = (number_chrysanthemums * price_chrysanthemums + number_roses * price_roses + number_tulips *
                         price_tulips)
        if number_roses >= 10:
            price_bouquet -= price_bouquet * 0.10
        if total_flowers > 20:
            price_bouquet -= price_bouquet * 0.20

total_price_flowers = price_bouquet + price_arrangement

print(f"{total_price_flowers:.2f}")
