number_judges = int(input())

total_students_score = 0
number_grades = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        average_score = total_students_score / number_grades if number_grades > 0 else 0
        print(f"Student's final assessment is {average_score}.")
        break

    sum_grades = 0

    for judge in range(number_judges):
        new_grade = float(input())
        sum_grades += new_grade

    average_presentation_score = sum_grades / number_judges
    total_students_score += average_presentation_score
    number_grades += 1

    print(f"{presentation_name} - {average_presentation_score}.")