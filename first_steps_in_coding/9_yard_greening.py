square_meters_for_greening = float(input())

final_price = square_meters_for_greening * 7.61
discount = final_price * 0.18

final_price_service = final_price - discount

print(f"The final price is: {final_price_service} lv.")
print(f"The discount is: {discount} lv.")