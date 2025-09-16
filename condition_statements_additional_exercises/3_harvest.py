from math import ceil, floor

wine_yard_area = int(input())
grape_per_sq_m = float(input())
wine_needed_for_sell = int(input())
workers_number = int(input())

harvest = wine_yard_area * grape_per_sq_m
kg_grapes_for_wine = harvest * 0.4
grape_needed_per_liter_wine = 2.5
produced_wine = kg_grapes_for_wine / grape_needed_per_liter_wine

if produced_wine < wine_needed_for_sell:
    print(f"It will be a tough winter! More {floor(wine_needed_for_sell - produced_wine)} liters wine needed.")

elif produced_wine >= wine_needed_for_sell:
    print(f"Good harvest this year! Total wine: {ceil(produced_wine)} liters.")
    print(f"{ceil(produced_wine - wine_needed_for_sell)} liters left -> "
          f"{ceil((produced_wine - wine_needed_for_sell) / workers_number)} liters per person.")

