from math import ceil

number_of_days = int(input())
km_day_one = float(input())

goal = 1000
total_km = km_day_one
km_run = km_day_one

for day in range(1, number_of_days + 1):
    percentage = float(input())
    km_day_two = km_run + km_run * percentage / 100
    total_km += km_day_two
    km_run = km_day_two

if total_km >= goal:
    print(f"You've done a great job running {ceil(total_km - goal)} more kilometers!")
elif total_km < goal:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(goal - total_km)} more kilometers")
