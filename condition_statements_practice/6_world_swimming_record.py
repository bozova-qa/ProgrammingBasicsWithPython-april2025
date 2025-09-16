from math import floor

world_record = float(input())
swimming_distance = float(input())
time_per_meter = float(input())

new_record = swimming_distance * time_per_meter

if swimming_distance >= 15:
    water_resistance = floor(swimming_distance / 15)
    new_record += 12.5 * water_resistance

if new_record < world_record:
    print(f"Yes, he succeeded! The new world record is {new_record:.2f} seconds.")

elif new_record >= world_record:
    print(f"No, he failed! He was {new_record - world_record:.2f} seconds slower.")
