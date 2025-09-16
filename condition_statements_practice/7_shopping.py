budget_petar = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram_memory = int(input())

price_video_cards = 250 * number_video_cards
price_processor = price_video_cards * 0.35
price_ram = price_video_cards * 0.1

total_price = price_video_cards + price_processor * number_processors + price_ram * number_ram_memory

if number_video_cards > number_processors:
    discount = total_price * 0.15
    total_price -= discount

if total_price <= budget_petar:
    print(f"You have {budget_petar - total_price:.2f} leva left!")
elif total_price >= budget_petar:
    print(f"Not enough money! You need {total_price - budget_petar:.2f} leva more!")

