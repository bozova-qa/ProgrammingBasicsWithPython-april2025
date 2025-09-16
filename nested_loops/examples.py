n = 10

flag = False

for i in range(n):
    for j in range(n):
        if i + j == n:
            print(i + j)
            flag = True
            break
    if flag:
        break

