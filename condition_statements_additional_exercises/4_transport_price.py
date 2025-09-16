km_number = int(input())
day_time = str(input())

taxi_start_fee = 0.70
taxi_day_fee = 0.79
taxi_night_fee = 0.90

bus_fee = 0.09
train_fee = 0.06

if km_number < 20 and day_time == "day":
    print(f"{taxi_start_fee + km_number * taxi_day_fee:.2f}")
elif km_number < 20 and day_time == "night":
    print(f"{taxi_start_fee + km_number * taxi_night_fee:.2f}")

if 20 <= km_number < 100:
    print(f"{km_number * bus_fee:.2f}")
elif km_number >= 100:
    print(f"{km_number * train_fee:.2f}")
