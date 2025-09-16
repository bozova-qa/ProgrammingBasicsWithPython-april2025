pens = int(input())
markers = int(input())
detergent = int(input())
discount = int(input())

one_pack_of_pens_price = 5.80
one_pack_of_markers_price = 7.20
one_liter_of_detergent_price = 1.20

total_cost_pens = pens * one_pack_of_pens_price
total_cost_markers = markers * one_pack_of_markers_price
total_cost_detergent = detergent * one_liter_of_detergent_price

total_costs = total_cost_pens + total_cost_markers + total_cost_detergent
total_costs_with_discount = total_costs - (total_costs * discount / 100)

print (total_costs_with_discount)

