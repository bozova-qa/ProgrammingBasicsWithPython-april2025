from sys import maxsize
entry = input()

max_number = - maxsize

while entry != "Stop":
    n = int(entry)
    if n >= max_number:
        max_number = n
    entry = input()

print(max_number)


