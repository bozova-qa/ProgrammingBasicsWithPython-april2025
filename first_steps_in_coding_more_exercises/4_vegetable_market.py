price_vegetables = float(input())
price_fruit = float(input())
kg_vegetables = int(input())
kg_fruit = int(input())

eur_to_lv = 1.94

total_profit = price_vegetables * kg_vegetables + price_fruit * kg_fruit
total_profit_euro = total_profit / eur_to_lv

print(f"{total_profit_euro:.2f}")