name = input()
year = 1
sum_grades = 0
excluded = 0

while year <= 12:
    grade = float(input())
    if grade < 4.00:
        excluded += 1
        if excluded == 2:
            print(f"{name} has been excluded at {year} grade")
            break
        continue
    sum_grades += grade
    year += 1

else:
    average = sum_grades / 12
    print(f"{name} graduated. Average grade: {average:.2f}")
