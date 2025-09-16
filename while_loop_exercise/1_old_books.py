fav_book = input()

total_books = 0

book = input()

while book != fav_book and book != "No More Books":
    total_books += 1
    book = input()

if book == fav_book:
    print(f"You checked {total_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {total_books} books.")



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