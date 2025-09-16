weight_in_kg = float(input())
type_delivery = str(input())
distance_in_km = int(input())


if type_delivery == "standard":
    if 0 < weight_in_kg < 1:
        price_per_km = 0.03
        price_transport = distance_in_km * price_per_km
    elif 1 <= weight_in_kg < 10:
        price_per_km = 0.05
        price_transport = distance_in_km * price_per_km
    elif 10 <= weight_in_kg < 40:
        price_per_km = 0.10
        price_transport = distance_in_km * price_per_km
    elif 40 <= weight_in_kg < 90:
        price_per_km = 0.15
        price_transport = distance_in_km * price_per_km
    elif 90 <= weight_in_kg < 150:
        price_per_km = 0.20
        price_transport = distance_in_km * price_per_km
elif type_delivery == "express":
    if 0 < weight_in_kg < 1:
        overcharge_per_kg = 0.03 * 0.80
        overcharge_per_km = weight_in_kg * overcharge_per_kg
        total_overcharge = distance_in_km * overcharge_per_km
        price_transport = 0.03 * distance_in_km + total_overcharge
    elif 1 <= weight_in_kg < 10:
        overcharge_per_kg = 0.05 * 0.40
        overcharge_per_km = weight_in_kg * overcharge_per_kg
        total_overcharge = distance_in_km * overcharge_per_km
        price_transport = 0.05 * distance_in_km + total_overcharge
    elif 10 <= weight_in_kg < 40:
        overcharge_per_kg = 0.10 * 0.05
        overcharge_per_km = weight_in_kg * overcharge_per_kg
        total_overcharge = distance_in_km * overcharge_per_km
        price_transport = 0.10 * distance_in_km + total_overcharge
    elif 40 <= weight_in_kg < 90:
        overcharge_per_kg = 0.15 * 0.02
        overcharge_per_km = weight_in_kg * overcharge_per_kg
        total_overcharge = distance_in_km * overcharge_per_km
        price_transport = 0.15 * distance_in_km + total_overcharge
    elif 90 <= weight_in_kg < 150:
        overcharge_per_kg = 0.20 * 0.01
        overcharge_per_km = weight_in_kg * overcharge_per_kg
        total_overcharge = distance_in_km * overcharge_per_km
        price_transport = 0.20 * distance_in_km + total_overcharge

print(f"The delivery of your shipment with weight of {weight_in_kg:.3f} kg. would cost {price_transport:.2f} lv.")
