num_1 = int(input())
num_2 = int(input())

for num in range(num_1, num_2+1):
    sum_even = 0
    sum_odd = 0
    for index, digit in enumerate(str(num)):  # числото го правим в str, за да можем да вземем позиции.
        if index % 2 == 0:
            sum_even += int(digit)
        elif index % 2 != 0:
            sum_odd += int(digit)

    if sum_even == sum_odd:
        print(num, end=" ")

