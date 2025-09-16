pocket_money_per_day = float(input())
sales_money_per_day = float(input())
expenses = float(input())
present_price = float(input())

days = 5

saved_pocket_money = pocket_money_per_day * days
saved_sales_money = sales_money_per_day * days
total_money = saved_pocket_money + saved_sales_money
total_money -= expenses

if total_money >= present_price:
    print(f"Profit: {total_money:.2f} BGN, the gift has been purchased.")
elif total_money < present_price:
    print(f"Insufficient money: {(present_price - total_money):.2f} BGN.")
