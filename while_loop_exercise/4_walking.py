entry = input()

total_steps = 0

while entry != "Going home":
    steps = int(entry)
    total_steps += steps
    if total_steps > 10000:
        print("Goal reached! Good job!")
        print(f"{total_steps - 10000} steps over the goal!")
        break
    entry = input() # IMPORTANT!

if entry == "Going home":
    home_steps = int(input())
    total_steps += home_steps
    if total_steps >= 10000:
        print("Goal reached! Good job!")
        print(f"{total_steps - 10000} steps over the goal!")
    elif total_steps < 10000:
        print(f"{10000 - total_steps} more steps to reach goal.")

#or:
goal = 10000
steps_walked = 0

while True:
    new_input = input()
    if new_input == "Going home":
        steps_walked += int(input())
        if steps_walked < goal:
            print(f"{goal - steps_walked} more steps to reach goal.")
        else:
            print("Goal reached! Good job!")
            print(f"{steps_walked - goal} steps over the goal!")
        break

    steps_walked += int(new_input)

    if steps_walked >= goal:
        print("Goal reached! Good job!")
        print(f"{steps_walked - goal} steps over the goal!")
        break

###
steps_goal = 10000

total_steps = 0

while True:
    steps = input()
    if steps == "Going home":
        steps_home = int(input())
        total_steps += steps_home
        if total_steps >= steps_goal:
            print("Goal reached! Good job!")
            print(f"{total_steps - steps_goal} steps over the goal!")
            break
        else:
            print(f"{steps_goal - total_steps} more steps to reach goal.")
            break

    new_steps = int(steps)
    total_steps += new_steps

    if total_steps >= steps_goal:
        print("Goal reached! Good job!")
        print(f"{total_steps - steps_goal} steps over the goal!")




