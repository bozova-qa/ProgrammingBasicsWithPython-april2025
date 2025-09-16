character = str(input())

command = str()
command_counter = 0
word = ""

while True:
    if character == "End":
        print(word)

    new_character = str(input())

    if new_character == "c" or new_character == "o" or new_character == "n":
        command_counter += 1
        word += character
        if command_counter == 2:
            word += new_character
            print(word)
    else:
        word += character
#            break



