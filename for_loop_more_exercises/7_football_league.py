stadium_capacity = int(input())
total_number_fans = int(input())

counter_a = 0
counter_b = 0
counter_v = 0
counter_g = 0

for fan in range(1, total_number_fans + 1):
    new_fan = str(input())

    if new_fan == "A":
        counter_a += 1
    elif new_fan == "B":
        counter_b += 1
    elif new_fan == "V":
        counter_v += 1
    elif new_fan == "G":
        counter_g += 1

print(f"{counter_a / total_number_fans * 100:.2f}%")
print(f"{counter_b / total_number_fans * 100:.2f}%")
print(f"{counter_v / total_number_fans * 100:.2f}%")
print(f"{counter_g / total_number_fans * 100:.2f}%")
print(f"{total_number_fans / stadium_capacity * 100:.2f}%")

