budget = float(input())
season = str(input())

money_spent = 0

if season == "summer":
    if budget <= 100:
        money_spent = budget * 0.30
        print("Somewhere in Bulgaria")
        print(f"Camp - {money_spent:.2f}")
    elif budget <= 1000:
        money_spent = budget * 0.40
        print("Somewhere in Balkans")
        print(f"Camp - {money_spent:.2f}")
    elif budget > 1000:
        money_spent = budget * 0.90
        print("Somewhere in Europe")
        print(f"Hotel - {money_spent:.2f}")
elif season == "winter":
    if budget <= 100:
        money_spent = budget * 0.70
        print("Somewhere in Bulgaria")
        print(f"Hotel - {money_spent:.2f}")
    elif budget <= 1000:
        money_spent = budget * 0.80
        print("Somewhere in Balkans")
        print(f"Hotel - {money_spent:.2f}")
    elif budget > 1000:
        money_spent = budget * 0.90
        print("Somewhere in Europe")
        print(f"Hotel - {money_spent:.2f}")

