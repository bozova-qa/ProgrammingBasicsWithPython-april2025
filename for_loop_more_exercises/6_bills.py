number_of_months = int(input())

electricity_bill = 0
water_bill = 0
internet_bill = 0
other_bills = 0

for month in range(1, number_of_months + 1):
    new_bill = float(input())

    electricity_bill += new_bill
    water_bill += 20
    internet_bill += 15
    other_bills += (new_bill + 20 + 15) + (new_bill + 20 + 15) * 0.20
    average = (electricity_bill + water_bill + internet_bill + other_bills) / number_of_months

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {other_bills:.2f} lv")
print(f"Average: {average:.2f} lv")