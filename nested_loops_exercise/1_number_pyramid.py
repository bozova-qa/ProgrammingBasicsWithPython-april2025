n = int(input())
current_number = 1

for row in range(1, n + 1):  #определя колко реда да се отпечатат
    for col in range(1, row + 1):  # по колко числа да има на ред;print row number of elements, колоната слиза на долния ред, row не може да бъде
                                 # като поредходното число
        if current_number > n:
            break
        print(current_number, end=" ")  # принтираме първото, второто и т.н. число
        current_number += 1

    print()  # Move to next line after finishing a row

#n = 7
#for i in range(1, n + 1):
#    for j in range(1, i + 1):
#        print(j, end=' ')
#    print()
