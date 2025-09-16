n = int(input())
reversed_digits = []

while n > 0:
    digit = n % 10
    reversed_digits.append(digit)
    n //= 10

if len(reversed_digits) == 3:
    a, b, c = reversed_digits
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                print(f"{i} * {j} * {k} = {i * j * k};")
else:
    print("Please enter a 3-digit number.")