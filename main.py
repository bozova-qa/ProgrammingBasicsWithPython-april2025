number = float(input())

while number >= 0:
    new_number = number * 2
    print(f"Result: {new_number:.2f}")
    number = float(input())
else:
    print("Negative number!")


looking_for = input()

book_counter = 0

while True:
    new_input = input()
    if new_input == looking_for:
        print(f"You checked {book_counter} books and found it.")
        break

    if new_input == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_counter} books.")

    book_counter += 1