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