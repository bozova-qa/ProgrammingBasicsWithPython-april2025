budget = float(input())
season = str(input())

total_price_vacation = 0

if budget <= 1000:
    if season == "Summer":
       total_price_vacation = budget * 0.65
       print(f"Alaska - Camp - {total_price_vacation:.2f}")

    elif season == "Winter":
        total_price_vacation = budget * 0.45
        print(f"Morocco - Camp - {total_price_vacation:.2f}")

elif 1000 < budget <= 3000:
    if season == "Summer":
        total_price_vacation = budget * 0.80
        print(f"Alaska - Hut - {total_price_vacation:.2f}")

    elif season == "Winter":
        total_price_vacation = budget * 0.60
        print(f"Morocco - Hut - {total_price_vacation:.2f}")
elif budget > 3000:
    if season == "Summer":
        total_price_vacation = budget * 0.90
        print(f"Alaska - Hotel - {total_price_vacation:.2f}")

    elif season == "Winter":
        total_price_vacation = budget * 0.90
        print(f"Morocco - Hotel - {total_price_vacation:.2f}")
