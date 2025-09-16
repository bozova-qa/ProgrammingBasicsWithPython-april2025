N = int(input())
is_found = False

for number in range(1111, 9999):
    number_to_string = str(number)
    for digit in number_to_string: # НОВО!!!
        if int(digit) == 0: #wtf! защото на 0 не може да се дели
            is_found = False
            break
        elif N % int(digit) == 0:
            is_found = True
        else:
            is_found = False
            break

    if is_found: #  част от външния цикъл
        print(number, end=" ")
