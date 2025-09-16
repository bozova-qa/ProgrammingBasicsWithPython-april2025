entry_one = int(input())
entry_two = int(input())

cake_area = entry_one * entry_two

while True:
    piece = input()
    if piece == "STOP": # read as string to check for "STOP"
        print(f"{(cake_area / 1):.0f} pieces are left.")
        break

    new_piece = int(piece) # convert to int after confirming it's not "STOP"
    cake_area -= new_piece

    if cake_area < 0:
        print(f"No more cake left! You need {abs(cake_area):.0f} pieces more.")
        break

