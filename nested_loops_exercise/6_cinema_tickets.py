tickets_sold = 0
student_tickets_sold = 0
standard_tickets_sold = 0
kid_tickets_sold = 0

while True:
    movie = input()
    if movie == "Finish":
        break

    free_spaces = int(input())
    taken_spaces = 0

    while taken_spaces < free_spaces:
        type_of_the_ticket = input()

        if type_of_the_ticket == "End":
            break

        if type_of_the_ticket == "student":
            student_tickets_sold += 1
        elif type_of_the_ticket == "standard":
            standard_tickets_sold += 1
        elif type_of_the_ticket == "kid":
            kid_tickets_sold += 1

        taken_spaces += 1
        tickets_sold += 1

    print(f"{movie} - {((taken_spaces / free_spaces) * 100):.2f}% full.")

print(f"Total tickets: {tickets_sold}")
print(f"{((student_tickets_sold / tickets_sold) * 100):.2f}% student tickets.")
print(f"{((standard_tickets_sold / tickets_sold) * 100):.2f}% standard tickets.")
print(f"{((kid_tickets_sold / tickets_sold) * 100):.2f}% kids tickets.")
