number_of_students = int(input())

counter_top = 0
counter_4 = 0
counter_3 = 0
counter_fail = 0
counter_new_student = 0

for _ in range(number_of_students):
    new_student = float(input())
    counter_new_student += new_student
    if 2 <= new_student <= 2.99:
        counter_fail += 1
    elif 3 <= new_student <= 3.99:
        counter_3 += 1
    elif 4 <= new_student <= 4.99:
        counter_4 += 1
    else:
        counter_top += 1

average_grade = counter_new_student / number_of_students

print(f"Top students: {(counter_top / number_of_students) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(counter_4 / number_of_students) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(counter_3 / number_of_students) * 100:.2f}%")
print(f"Fail: {(counter_fail / number_of_students) * 100:.2f}%")
print(f"Average: {average_grade:.2f}")
