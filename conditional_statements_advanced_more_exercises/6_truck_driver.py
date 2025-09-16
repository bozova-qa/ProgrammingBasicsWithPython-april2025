season = str(input())
km_per_month = float(input())

taxes = 0.10
salary = 0

if season == "Spring":
    if km_per_month <= 5000:
        salary = km_per_month * 0.75 * 4
        salary -= salary * taxes
    elif 5000 < km_per_month <= 10000:
        salary = km_per_month * 0.95 * 4
        salary -= salary * taxes
    elif 10000 < km_per_month <= 20000:
        salary = km_per_month * 1.45 * 4
        salary -= salary * taxes
elif season == "Autumn":
    if km_per_month <= 5000:
        salary = km_per_month * 0.75 * 4
        salary -= salary * taxes
    elif 5000 < km_per_month <= 10000:
        salary = km_per_month * 0.95 * 4
        salary -= salary * taxes
    elif 10000 < km_per_month <= 20000:
        salary = km_per_month * 1.45 * 4
        salary -= salary * taxes
elif season == "Summer":
    if km_per_month <= 5000:
        salary = km_per_month * 0.90 * 4
        salary -= salary * taxes
    elif 5000 < km_per_month <= 10000:
        salary = km_per_month * 1.10 * 4
        salary -= salary * taxes
    elif 10000 < km_per_month <= 20000:
        salary = km_per_month * 1.45 * 4
        salary -= salary * taxes
elif season == "Winter":
    if km_per_month <= 5000:
        salary = km_per_month * 1.05 * 4
        salary -= salary * taxes
    elif 5000 < km_per_month <= 10000:
        salary = km_per_month * 1.25 * 4
        salary -= salary * taxes
    elif 10000 < km_per_month <= 20000:
        salary = km_per_month * 1.45 * 4
        salary -= salary * taxes

print(f"{salary:.2f}")
