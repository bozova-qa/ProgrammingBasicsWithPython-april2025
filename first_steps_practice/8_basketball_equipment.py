annual_fee = int(input())

price_for_shoes = annual_fee - (annual_fee * 0.4)
price_for_clothes = price_for_shoes - (price_for_shoes * 0.2)
price_for_basketball = price_for_clothes * 0.25
price_accessory = price_for_basketball * 0.2

total_cost = annual_fee + price_for_shoes + price_for_clothes + price_for_basketball + price_accessory

print(total_cost)

