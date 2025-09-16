lily_age = int(input())
price_washing_machine = float(input())
toy_single_price = int(input())

total_money_present = 0
total_money_toy = 0
money_present = 0

for year in range(1, lily_age + 1):
    if year % 2 != 0:
        total_money_toy += toy_single_price
    elif year % 2 == 0:
        money_present += 10 # ще се увеличава с 10, ако е само = 10, остава същата сума
        total_money_present += money_present - 1

total_money = total_money_present + total_money_toy

if total_money >= price_washing_machine:
    print(f"Yes! {total_money - price_washing_machine:.2f}")
elif total_money <= price_washing_machine:
    print(f"No! {price_washing_machine - total_money:.2f}")
