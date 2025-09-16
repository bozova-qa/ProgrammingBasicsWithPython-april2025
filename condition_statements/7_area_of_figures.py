from math import pi

type_figure = str(input())

if type_figure == "square":
    side_square = float(input())
    area_square = side_square * side_square
    print(f"{area_square:.3f}")

elif type_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area_rectangle = side_a * side_b
    print(f"{area_rectangle:.3f}")

elif type_figure == "circle":
    radius = float(input())
    area_circle = pi * radius * radius # or pi * radius ** 2
    print(f"{area_circle:.3f}")

elif type_figure == "triangle":
    side_length = float(input())
    height = float(input())
    area_triangle = (side_length * height)/2
    print(f"{area_triangle:.3f}")
