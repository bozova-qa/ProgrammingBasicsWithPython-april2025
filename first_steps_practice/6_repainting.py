protective_foil = int(input())
paint = int(input())
thinner = int(input())
working_hours = int(input())

price_for_foil = 1.50
price_for_paint = 14.50
price_for_thinner_per_liter = 5
price_for_bags = 0.40

cost_protective_foil = (protective_foil + 2) * price_for_foil
cost_paint = (paint + paint * 0.1) * price_for_paint
cost_thinner = thinner * price_for_thinner_per_liter
cost_for_bags = 0.40

total_cost_materials = cost_protective_foil + cost_paint + cost_thinner + cost_for_bags
total_cost_paint_job = working_hours * total_cost_materials * 0.30
total_cost = total_cost_materials + total_cost_paint_job

print(total_cost)

