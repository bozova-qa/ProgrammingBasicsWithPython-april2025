actors_name = str(input())
academy_points = float(input())
number_judges = int(input())

coefficient = 1
flag = True

actors_points = 0
total_points = 0

for judge in range(1, number_judges + 1):
    judge_name = str(input())
    judge_points = float(input())
    length = len(judge_name)
    actors_points += (length * judge_points) / 2
    total_points = academy_points + actors_points
    coefficient += 1

    if total_points > 1250.5:
        print(f"Congratulations, {actors_name} got a nominee for leading role with {total_points:.1f}!")
        flag = False
        break

if total_points <= 1250.5:
    print(f"Sorry, {actors_name} you need {1250.5 - total_points:.1f} more!")

