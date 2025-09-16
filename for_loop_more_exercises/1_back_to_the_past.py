money_inherited = float(input())
final_year = int(input())

age = 18
money_spent = 0

for year in range(1800, final_year + 1):
    if year % 2 == 0:
        money_spent += 12000.00
        age += 1 # възраст се сменя и в двата случая
    elif year % 2 != 0:
        money_spent += 12000.00 + 50 * age
        age += 1 # възраст се сменя и в двата случая

money_left = money_inherited - money_spent

if money_left >= 0:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
elif money_left < 0:
    print(f"He will need {abs(money_left):.2f} dollars to survive.")
