number_of_turns = int(input())

total_points = 0
is_valid = True
counter_one = 0
counter_two = 0
counter_three = 0
counter_four = 0
counter_five = 0
counter_six = 0

for _ in range(number_of_turns):
    new_number = int(input())

    if new_number < 0:
        is_valid = False
        total_points /= 2
        counter_six += 1
    elif 0 <= new_number <= 9:
        total_points += 0.20 * new_number
        counter_one += 1
    elif 10 <= new_number <= 19:
        total_points += 0.30 * new_number
        counter_two += 1
    elif 20 <= new_number <= 29:
        total_points += 0.40 * new_number
        counter_three += 1
    elif 30 <= new_number <= 39:
        total_points += 50
        counter_four += 1
    elif 40 <= new_number <= 50:
        total_points += 100
        counter_five += 1
    else:
        is_valid = False
        total_points /= 2
        counter_six += 1

print(f"{total_points:.2f}")
print(f"From 0 to 9: {(counter_one / number_of_turns) * 100:.2f}%")
print(f"From 10 to 19: {(counter_two / number_of_turns) * 100:.2f}%")
print(f"From 20 to 29: {(counter_three / number_of_turns) * 100:.2f}%")
print(f"From 30 to 39: {(counter_four / number_of_turns) * 100:.2f}%")
print(f"From 40 to 50: {(counter_five / number_of_turns) * 100:.2f}%")
print(f"Invalid numbers: {(counter_six / number_of_turns) * 100:.2f}%")

