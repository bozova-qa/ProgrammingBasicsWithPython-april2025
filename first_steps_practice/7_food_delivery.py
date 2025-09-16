number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())
number_of_desserts = number_of_chicken_menus + number_of_fish_menus + number_of_vegetarian_menus

price_chicken = 10.35
price_fish = 12.40
price_vegetarian = 8.15
price_dessert = (number_of_chicken_menus * price_chicken + number_of_fish_menus * price_fish +
                + number_of_vegetarian_menus * price_vegetarian) * 0.20
delivery_cost = 2.50

cost_chicken = number_of_chicken_menus * price_chicken
cost_fish = number_of_fish_menus * price_fish
cost_vegetarian = number_of_vegetarian_menus * price_vegetarian

total_check = cost_chicken + cost_fish + cost_vegetarian + price_dessert + delivery_cost

print(total_check)

