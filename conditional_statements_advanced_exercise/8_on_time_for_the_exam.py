exam_start_hour = int(input())
exam_start_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

total_minutes_start_exam = (exam_start_hour * 60) + exam_start_minutes
total_minutes_arrival = (arrival_hour * 60) + arrival_minutes
difference = total_minutes_start_exam - total_minutes_arrival

if difference == "0":
    print("On time")
elif 0 <= difference <= 30:
    print("On time")
    print(f"{difference} minutes before the start")
elif 30 < difference <= 59:
    print("Early")
    print(f"{difference} minutes before the start")

elif difference > 59:
    hours = difference // 60
    minutes = difference % 60
    print("Early")
    if minutes < 10:
        print(f"{hours}:0{minutes} hours before the start")
    else:
        print(f"{hours}:{minutes} hours before the start")

elif -59 <= difference < 0:
    print("Late")
    print(f"{abs(difference)} minutes after the start")
elif difference <= -60:
    hours = abs(difference) // 60
    minutes = abs(difference) % 60
    print("Late")
    if minutes < 10:
        print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")




