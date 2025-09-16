type_fuel = str(input())
fuel_in_tank = float(input())

is_valid = True

if fuel_in_tank >= 25:
    if type_fuel == "Diesel":
        print("You have enough diesel.")
    elif type_fuel == "Gasoline":
        print("You have enough gasoline.")
    elif type_fuel == "Gas":
        print("You have enough gas.")
    else:
        is_valid = False

if fuel_in_tank < 25:
    if type_fuel == "Diesel":
        print("Fill your tank with diesel!")
    elif type_fuel == "Gasoline":
        print("Fill your tank with gasoline!")
    elif type_fuel == "Gas":
        print("Fill your tank with gas!")
    else:
        is_valid = False

if not is_valid:
    print("Invalid fuel!")


