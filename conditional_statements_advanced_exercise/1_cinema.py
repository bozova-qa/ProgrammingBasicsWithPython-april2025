type_screening = str(input())
number_rows = int(input())
number_columns = int(input())

total_price = 0

if type_screening == "Premiere":
    total_price = number_rows * number_columns * 12
elif type_screening == "Normal":
    total_price = number_rows * number_columns * 7.5
elif type_screening == "Discount":
    total_price = number_rows * number_columns * 5.0

print(f"{total_price:.2f} leva")
