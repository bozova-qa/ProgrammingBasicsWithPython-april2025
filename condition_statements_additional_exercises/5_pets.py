from math import ceil, floor

number_days = int(input())
food_left = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_g = float(input())

dog_food_needed = number_days * dog_food_per_day_kg
cat_food_needed = number_days * cat_food_per_day_kg
turtle_food_needed = number_days * turtle_food_per_day_g

total_food = dog_food_needed + cat_food_needed + turtle_food_needed / 1000

if food_left >= total_food:
    print(f"{floor(food_left - total_food)} kilos of food left.")
elif food_left < total_food:
    print(f"{ceil(total_food - food_left)} more kilos of food are needed.")
