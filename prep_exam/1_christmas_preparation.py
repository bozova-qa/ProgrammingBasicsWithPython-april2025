wrap_paper_rolls = int(input())
fabric_rolls = int(input())
liters_glue = float(input())
discount = int(input())

price_one_wrap_paper = 5.80
price_one_roll_fabric = 7.20
price_liter_glue = 1.20

price_wrap_paper = wrap_paper_rolls * price_one_wrap_paper
price_fabric = fabric_rolls * price_one_roll_fabric
price_glue = liters_glue * price_liter_glue

total_materials = price_wrap_paper + price_fabric + price_glue

total_materials -= total_materials * (discount / 100)

print(f"{total_materials:.3f}")
