from math import ceil, floor

number_magnolias = int(input())
number_hyacinth = int(input())
number_roses = int(input())
number_cactus = int(input())
present_price = float(input())

price_magnolias = 3.25
price_hyacinth = 4
price_roses = 3.50
price_cactus = 8

profit = number_magnolias * price_magnolias + number_hyacinth * price_hyacinth + number_roses * price_roses + \
        number_cactus * price_cactus

profit_after_taxes = profit - profit * 0.05

if profit_after_taxes >= present_price:
    print(f"She is left with {floor(profit_after_taxes - present_price)} leva.")
elif present_price > profit_after_taxes:
    print(f"She will have to borrow {ceil(present_price - profit_after_taxes)} leva.")
