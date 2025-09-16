days_counter = 1
total_meters_climbed = 5364
base_camp = 5364

while True:
    entry = input()
    if entry == "END":
        print(f"Failed!")
        print(f"{total_meters_climbed}")
        break
    if entry == "Yes":
        days_counter += 1
        if days_counter > 5:
            print("Failed!")
            print(f"{total_meters_climbed}")
            break
        meters_climbed = int(input())
        total_meters_climbed += meters_climbed
    if entry == "No":
        meters_climbed = int(input())
        total_meters_climbed += meters_climbed

    if total_meters_climbed >= 8848:
        print(f"Goal reached for {days_counter} days!")
        break
