total_days = int(input())

number_of_doctors = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, total_days + 1):
    if day % 3 == 0 and untreated_patients > treated_patients:
        number_of_doctors += 1

    number_patients_a_day = int(input())
    if number_patients_a_day <= number_of_doctors:
        treated_patients += number_patients_a_day
    elif number_patients_a_day > number_of_doctors:
        treated_patients += number_of_doctors
        untreated_patients += number_patients_a_day - number_of_doctors


print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
