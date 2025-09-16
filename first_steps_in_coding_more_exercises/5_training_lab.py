length = float(input())
width = float(input())

room_width_cm = width * 100
room_length_cm = length * 100
desk_width = 70
desk_length = 120

usable_width = room_width_cm - 100
number_rows = usable_width // desk_width

number_rows_length = room_length_cm // desk_length

number_work_spaces = number_rows * number_rows_length - 3

print(number_work_spaces)


