budget = float(input())
season = str(input())

rent_price = 0

if budget <= 100:
    if season == "Summer":
        print("Economy class")
        rent_price = budget * 0.35
        print(f"Cabrio - {rent_price:.2f}")
    elif season == "Winter":
        print("Economy class")
        rent_price = budget * 0.65
        print(f"Jeep - {rent_price:.2f}")
elif 100 < budget <= 500:
    if season == "Summer":
        print("Compact class")
        rent_price = budget * 0.45
        print(f"Cabrio - {rent_price:.2f}")
    elif season == "Winter":
        print("Compact class")
        rent_price = budget * 0.80
        print(f"Jeep - {rent_price:.2f}")
elif budget > 500:
    if season == "Summer" or season == "Winter":
        print("Luxury class")
        rent_price = budget * 0.90
        print(f"Jeep - {rent_price:.2f}")

