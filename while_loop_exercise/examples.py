expected_sales = int(input())

payment_counter = 0
total_sales = 0
total_cash_sum = 0
total_card_sum = 0
cash_counter = 0
card_counter = 0

while True:
    entry = input()
    if entry == "End":
        print("Failed to collect required money for charity.")
        break

    payment = int(entry)
    payment_counter += 1

    if payment_counter % 2 != 0:
        # Cash payment
        if payment > 100:
            print("Error in transaction!")
        elif 10 <= payment <= 100 or payment < 10:
            total_cash_sum += payment
            cash_counter += 1
            total_sales += payment
            print("Product sold!")
    else:
        # Card payment
        if payment > 100:
            total_card_sum += payment
            card_counter += 1
            total_sales += payment
            print("Product sold!")
        elif 10 <= payment <= 100 or payment < 10:
            print("Error in transaction!")

    if total_sales >= expected_sales:
        average_cash = total_cash_sum / cash_counter if cash_counter > 0 else 0
        average_card = total_card_sum / card_counter if card_counter > 0 else 0
        print(f"Average CS: {average_cash:.2f}")
        print(f"Average CC: {average_card:.2f}")
        break


