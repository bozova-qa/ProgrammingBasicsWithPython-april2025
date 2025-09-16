import sys

n = int(input())

max_number = -sys.maxsize
sum_numbers = 0

for num in range(n):
    new_num = int(input())
    if new_num > max_number:
        max_number = new_num

    sum_numbers += new_num

if max_number == (sum_numbers - max_number):
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(max_number - (sum_numbers - max_number))}")
