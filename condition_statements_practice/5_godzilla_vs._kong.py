film_budget = float(input())
film_extras = int(input())
wardrobe_price_per_person = float(input())

decor_price = film_budget * 0.1
total_wardrobe_price = film_extras * wardrobe_price_per_person
total_price = decor_price + total_wardrobe_price

if film_extras > 150:
    discount = total_wardrobe_price * 0.1
    total_price -= discount

if total_price > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {total_price - film_budget:.2f} leva more.")
if total_price <= film_budget:
    print("Action!")
    print(f"Wingard starts filming with {film_budget - total_price:.2f} leva left.")
