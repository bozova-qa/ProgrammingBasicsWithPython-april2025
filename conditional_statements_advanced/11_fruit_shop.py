fruit = str(input())
day = str(input())
quantity = float(input())

is_valid = True

total_price = 0

if (day == "Monday"
    or day == "Tuesday"
    or day == "Wednesday"
    or day == "Thursday"
        or day == "Friday"):
    if fruit == "banana":
        total_price = quantity * 2.50
    elif fruit == "apple":
        total_price = quantity * 1.20
    elif fruit == "orange":
        total_price = quantity * 0.85
    elif fruit == "grapefruit":
        total_price = quantity * 1.45
    elif fruit == "kiwi":
        total_price = quantity * 2.70
    elif fruit == "pineapple":
        total_price = quantity * 5.50
    elif fruit == "grapes":
        total_price = quantity * 3.85
    else:
        is_valid = False

elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        total_price = quantity * 2.70
    elif fruit == "apple":
        total_price = quantity * 1.25
    elif fruit == "orange":
        total_price = quantity * 0.90
    elif fruit == "grapefruit":
        total_price = quantity * 1.60
    elif fruit == "kiwi":
        total_price = quantity * 3.00
    elif fruit == "pineapple":
        total_price = quantity * 5.60
    elif fruit == "grapes":
        total_price = quantity * 4.20
    else:
        is_valid = False
else:
    is_valid = False

if not is_valid:
    print("error")
else:
    print(f"{total_price:.2f}")
