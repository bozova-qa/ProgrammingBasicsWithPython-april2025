vacation_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = 2.60
doll_price = 3.00
bear_price = 4.1
minion_price = 8.2
truck_price = 2.00

toy_order = puzzles + dolls + bears + minions + trucks
total_price = (puzzles * puzzle_price) + (dolls * doll_price) + (bears * bear_price) + (minions * minion_price)\
         + (trucks * truck_price)

if toy_order >= 50:
    discount = total_price * 0.25
    total_price -= discount

rent = total_price * 0.1
final_profit = total_price - rent

if final_profit >= vacation_price:
    print(f"Yes! {final_profit - vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - final_profit:.2f} lv needed.")
