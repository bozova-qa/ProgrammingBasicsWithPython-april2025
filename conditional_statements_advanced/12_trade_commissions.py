city = input()
sales = float(input())

commission = 0

is_valid = True

if city == "Sofia":
    if 0 <= sales <= 500:
        commission = sales * 0.05
    elif 500 < sales <= 1000:
        commission = sales * 0.07
    elif 1000 <= sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
    elif sales < 0:
        is_valid = False
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = sales * 0.045
    elif 500 < sales <= 1000:
        commission = sales * 0.075
    elif 1000 <= sales <= 10000:
        commission = sales * 0.1
    elif sales > 10000:
        commission = sales * 0.13
    elif sales < 0:
        is_valid = False
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = sales * 0.055
    elif 500 < sales <= 1000:
        commission = sales * 0.08
    elif 1000 <= sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145
    elif sales < 0:
        is_valid = False
else:
    is_valid = False

if not is_valid:
    print("error")
else:
    print(f"{commission:.2f}")
