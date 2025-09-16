washing_bottles = int(input())
total_detergent = washing_bottles * 750

used_detergent = 0
counter_washing_cycles = 0
counter_plates = 0
counter_pans = 0

while True:
    entry = input()
    if entry == "End":
        print("Detergent was enough!")
        print(f"{counter_plates} dishes and {counter_pans} pots were washed.")
        print(f"Leftover detergent {leftover_detergent} ml.")
        break

    number_items = int(entry)
    counter_washing_cycles += 1

    if counter_washing_cycles % 3 == 0:
        counter_pans += number_items
        used_detergent += number_items * 15
    else:
        counter_plates += number_items
        used_detergent += number_items * 5

    leftover_detergent = total_detergent - used_detergent

    if used_detergent > total_detergent:
        print(f"Not enough detergent, {abs(leftover_detergent)} ml. more necessary!")
        break
