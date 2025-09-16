length = int(input())
width = int(input())
height = int(input())
percentage_sand = float(input())

volume = length * width * height
volume_water_in_liters = length * width * height * 0.001

litters_needed = volume_water_in_liters * (1 - (percentage_sand / 100))

print(litters_needed)

