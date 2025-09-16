floors = int(input())
rooms = int(input())

result = ""

for floor in range(floors, 0, -1): # намаляват в низходящ ред
    for room in range(rooms):  # не намаляват в низходящ ред
        if floor == floors:  # ако има само един етаж
            result = f"L{floor}{room}"

        elif floor % 2 == 0:
            result = f"O{floor}{room}"

        elif floor % 2 != 0:
            result = f"A{floor}{room}"

        print(result, end=" ")
    print()  # принтира само нов ред за следващата итерация, без result
