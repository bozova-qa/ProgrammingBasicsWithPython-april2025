n = int(input())
num = 1 # the first number printed, will change in each loop

for i in range (0, n + 1, 2):
    print(num)
    num = num * 2 * 2 # So on each iteration, num becomes 4 times bigger than it was before.



