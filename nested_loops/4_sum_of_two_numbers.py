start_number = int(input())
end_number = int(input())
magic_number = int(input())

combinations_counter = 0
is_found_magic = False # в началото е False, защото не сме намерили magic number

for i in range(start_number, end_number + 1):
    for j in range(start_number, end_number + 1):
        combinations_counter += 1
        if i + j == magic_number:
            print(f"Combination N:{combinations_counter} "
                  f"({i} + {j} = {magic_number})")
            is_found_magic = True # break за вътрешен цикъл, намерили сме magic_number
            break

    if is_found_magic: # break за външен цикъл
        break
if not is_found_magic: # ако break_condition е false, не сме намерили magic_number
    print(f"{combinations_counter} combinations - neither equals {magic_number}")
