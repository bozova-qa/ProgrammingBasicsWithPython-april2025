word = input()

total_sum = 0

for index in range(0, len(word)):
    if word[index] == "a":
        total_sum += 1
    elif word[index] == "e":
        total_sum += 2
    elif word[index] == "i":
        total_sum += 3
    elif word[index] == "o":
        total_sum += 4
    elif word[index] == "u":
        total_sum += 5

print(total_sum)
