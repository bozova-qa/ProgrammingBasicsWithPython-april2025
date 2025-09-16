while True:  # We use while True: to loop until "End" is entered.
    destination = input()
    if destination == "End":  # We check if the input is "End" right after getting the destination.
        break

    min_budget = float(input())  # We reset min_budget after every destination
    savings = 0  # We reset savings = 0 for every new destination.

    while savings < min_budget:
        new_saving = float(input())
        savings += new_saving

    print(f"Going to {destination}!")
