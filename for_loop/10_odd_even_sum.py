n = int(input())

sum_even = 0
sum_odd = 0

for i in range(1, n + 1):
    number = int(input())
    if i % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

if sum_even == sum_odd:
    print(f"Yes\nSum = {sum_even}")
else:
    print(f"No\nDiff = {abs(sum_even - sum_odd)}")


