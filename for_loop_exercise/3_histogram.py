n = int(input())

sum_p1 = 0
sum_p2 = 0
sum_p3 = 0
sum_p4 = 0
sum_p5 = 0

for _ in range(n):
    new_number = int(input())
    if new_number < 200:
        sum_p1 += 1
    elif 200 <= new_number <= 399:
        sum_p2 += 1
    elif 400 <= new_number <= 599:
        sum_p3 += 1
    elif 600 <= new_number <= 799:
        sum_p4 += 1
    elif new_number >= 800:
        sum_p5 += 1

print(f"{(sum_p1 / n * 100):.2f}%")
print(f"{(sum_p2 / n * 100):.2f}%")
print(f"{(sum_p3 / n * 100):.2f}%")
print(f"{(sum_p4 / n * 100):.2f}%")
print(f"{(sum_p5 / n * 100):.2f}%")
