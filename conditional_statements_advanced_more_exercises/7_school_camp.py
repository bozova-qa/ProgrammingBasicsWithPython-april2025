season = str(input())
type_of_group = str(input())
number_students = int(input())
number_nights = int(input())

total_price = 0

if season == "Winter":
    if type_of_group == "girls":
        total_price = number_students * number_nights * 9.60
        if number_students >= 50:
            total_price -= total_price * 0.50
        elif 20 <= number_students < 50:
            total_price -= total_price * 0.15
        elif 10 <= number_students < 20:
            total_price -= total_price * 0.05
        print(f"Gymnastics {total_price:.2f} lv." )
    elif type_of_group == "boys":
        total_price = number_students * number_nights * 9.60
        if number_students >= 50:
            total_price -= total_price * 0.50
        elif 20 <= number_students < 50:
            total_price -= total_price * 0.15
        elif 10 <= number_students < 20:
            total_price -= total_price * 0.05
        print(f"Judo {total_price:.2f} lv." )
    elif type_of_group == "mixed":
        total_price = number_students * number_nights * 10
        if number_students >= 50:
            total_price -= total_price * 0.50
        elif 20 <= number_students < 50:
            total_price -= total_price * 0.15
        elif 10 <= number_students < 20:
            total_price -= total_price * 0.05
        print(f"Ski {total_price:.2f} lv." )
elif season == "Spring":
    if type_of_group == "girls":
        total_price = number_students * number_nights * 7.20
        if number_students >= 50:
            total_price -= total_price * 0.50
        elif 20 <= number_students < 50:
            total_price -= total_price * 0.15
        elif 10 <= number_students < 20:
            total_price -= total_price * 0.05
        print(f"Athletics {total_price:.2f} lv.")
    elif type_of_group == "boys":
        total_price = number_students * number_nights * 7.20
        if number_students >= 50:
            total_price -= total_price * 0.50
        elif 20 <= number_students < 50:
            total_price -= total_price * 0.15
        elif 10 <= number_students < 20:
            total_price -= total_price * 0.05
        print(f"Tennis {total_price:.2f} lv.")
    elif type_of_group == "mixed":
        total_price = number_students * number_nights * 9.50
        if number_students >= 50:
            total_price -= total_price * 0.50
        elif 20 <= number_students < 50:
            total_price -= total_price * 0.15
        elif 10 <= number_students < 20:
            total_price -= total_price * 0.05
        print(f"Cycling {total_price:.2f} lv.")
elif season == "Summer":
    if type_of_group == "girls":
        total_price = number_students * number_nights * 15
        if number_students >= 50:
            total_price -= total_price * 0.50
        elif 20 <= number_students < 50:
            total_price -= total_price * 0.15
        elif 10 <= number_students < 20:
            total_price -= total_price * 0.05
        print(f"Volleyball {total_price:.2f} lv.")
    elif type_of_group == "boys":
        total_price = number_students * number_nights * 15
        if number_students >= 50:
            total_price -= total_price * 0.50
        elif 20 <= number_students < 50:
            total_price -= total_price * 0.15
        elif 10 <= number_students < 20:
            total_price -= total_price * 0.05
        print(f"Football {total_price:.2f} lv.")
    elif type_of_group == "mixed":
        total_price = number_students * number_nights * 20
        if number_students >= 50:
            total_price -= total_price * 0.50
        elif 20 <= number_students < 50:
            total_price -= total_price * 0.15
        elif 10 <= number_students < 20:
            total_price -= total_price * 0.05
        print(f"Swimming {total_price:.2f} lv.")


