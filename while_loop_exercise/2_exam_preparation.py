max_poor_grades = int(input())

sum_grades = 0
total_tasks = 0
poor_grades = 0
last_task = ""

while True:
    task_name = input()
    if task_name == "Enough":
        average = sum_grades / total_tasks
        print(f"Average score: {average:.2f}")
        print(f"Number of problems: {total_tasks}")
        print(f"Last problem: {last_task}")
        break

    grade = int(input())

    if grade <= 4:
        poor_grades += 1
        if poor_grades == max_poor_grades:
            print(f"You need a break, {poor_grades} poor grades.")
            break

    sum_grades += grade
    total_tasks += 1
    last_task = task_name  ### Important!

#or:

max_fails = max_fails_counter = input()

total_tasks = total_tasks_score = 0
last_task = ""

while max_fails_counter > 0:
    new_task = input()

    if new_task == "Enough":
        if total_tasks == 0:
            print("Cannot calculate average score. There are still no tasks.")
            break
        print(f"Average score: {total_tasks_score / total_tasks:.2f}")
        print(f"Number of problems: {total_tasks}")
        print(f"Last problem: {last_task}")
        break

    last_task = new_task
    total_tasks += 1

    task_score = int(input())
    total_tasks_score += task_score

    if task_score <= 4:
        max_fails_counter -= 1
        if max_fails_counter <= 0:
            print(f"You need a break, {max_fails} poor grades.")
