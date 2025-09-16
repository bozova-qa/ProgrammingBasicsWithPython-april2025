hour = int(input())
day_of_week = str(input())

if hour in range(10, 18):
    if (day_of_week == "Monday" or
        day_of_week == "Tuesday" or
        day_of_week == "Wednesday" or
        day_of_week == "Thursday" or
        day_of_week == "Friday" or
            day_of_week == "Saturday"):
        print("open")
    else:
        print("closed")
else:
    print("closed")