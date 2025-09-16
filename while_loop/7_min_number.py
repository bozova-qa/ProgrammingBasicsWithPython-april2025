from sys import maxsize
entry = input()

min_number = maxsize

while entry != "Stop":
    n = int(entry)
    if n <= min_number:
        min_number = n
    entry = input()

print(min_number)
