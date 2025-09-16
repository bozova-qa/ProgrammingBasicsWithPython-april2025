number_judges = int(input())

total_students_score = 0
presentations_count = 0

while True:
    presentation_title = input()
    if presentation_title == "Finish":
        average_score = total_students_score / presentations_count if presentations_count > 0 else 0
        print(f"Student's final assessment is {average_score:.2f}.")
        break

    sum_grades = 0

    for _ in range(number_judges):
        new_grade = float(input())
        sum_grades += new_grade

    average_presentation_score = sum_grades / number_judges
    total_students_score += average_presentation_score
    presentations_count += 1

    print(f"{presentation_title} - {average_presentation_score:.2f}.")

# неточно

number_judges = int(input())

current_number_presentations = 0
total_presentations = 0
sum_grades = 0.0
total_students_score = 0
students_average = 0

while True:
    presentation_title = input()
    if presentation_title == "Finish":
        print(f"Student's final assessment is {total_students_score / total_presentations:.2f}.")
        break

    current_number_presentations = 0
    sum_grades = 0

    for _ in range(1, number_judges + 1):
        new_grade = float(input())
        sum_grades += new_grade
        total_students_score += new_grade
        current_number_presentations += 1
        total_presentations += 1

    average_presentation_score = sum_grades / current_number_presentations
    students_average += average_presentation_score

    print(f"{presentation_title} - {average_presentation_score:.2f}.")
