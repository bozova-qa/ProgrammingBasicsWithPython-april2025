number_goods = int(input())

total_goods = 0
bus_price = 0
truck_price = 0
train_price = 0

bus_counter = 0
truck_counter = 0
train_counter = 0


for _ in range(number_goods):
    new_good = int(input())
    total_goods += new_good

    if new_good <= 3:
        bus_price += new_good * 200
        bus_counter += new_good
    elif 4 <= new_good <= 11:
        truck_price += new_good * 175
        truck_counter += new_good
    elif new_good >= 12:
        train_price += new_good * 120
        train_counter += new_good

average_price_per_ton = (bus_price + truck_price + train_price) / total_goods

print(f"{average_price_per_ton:.2f}")
print(f"{bus_counter / total_goods * 100:.2f}%")
print(f"{truck_counter / total_goods * 100:.2f}%")
print(f"{train_counter / total_goods * 100:.2f}%")

