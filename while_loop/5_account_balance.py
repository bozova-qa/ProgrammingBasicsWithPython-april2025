entry = input()

total_sum = 0

while entry != "NoMoreMoney":
    deposit = float(entry)
    if deposit < 0:
        print("Invalid operation!")
        break
    else:
        total_sum += deposit
        print(f"Increase: {deposit:.2f}")
        entry = input()  # следващ депозит

print(f"Total: {total_sum:.2f}")


###

total_sum = 0

while True:
    entry = input()
    if entry == "NoMoreMoney":
        break

    deposit = float(entry)
    if deposit < 0:
        print("Invalid operation")
        break

    total_sum += deposit
    print(f"Increase: {deposit}")

print(f"Total sum: {total_sum:.2f}")