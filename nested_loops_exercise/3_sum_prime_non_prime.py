sum_prime_numbers = 0
sum_non_prime_numbers = 0

while True:
    non_prime_number = False
    new_input = input()
    if new_input == "stop":
        break

    new_number = int(new_input)

    if new_number < 0:
        print("Number is negative.")
        continue

    else:
        for number in range(2, int(new_number ** 0.5)+1):  # check up to √n to see if it's divisible by something.
            if new_number % number == 0:
                sum_non_prime_numbers += new_number
                non_prime_number = True
                break

    if not non_prime_number: # ако е False, тоест prime number
        sum_prime_numbers += new_number

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")
