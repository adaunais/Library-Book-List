import os

books = []

if os.path.exists("books.txt"):
    with open("books.txt", "r") as file: #opens file named "books.text" in read only mode
        books = [line.strip() for line in file.readlines()] #read every line in the file and removes leading and trailing spaces 

def save_books():
    with open("books.txt", 'w') as file:
        for book in books:
            file.write(book + "\n")

def view_books():
    if not books:
        print("\nYour book list is empty!\n")
        return
    print("\n--- BOOK LIST ---")
    for number, task in enumerate(books, start=1): #gives both the index and name of item in list, starts count at 1
        print(f"{number}. {task}")
    print()

def add_books():
    book = input("Enter the book: ").strip() #user input removes whitespace
    if book:
        books.append(book) #add to the end of the list
        print(f"Added book: {book}\n") #print statement 
        save_books() #save function , created above
    else:
        print("book cannot be empty!\n")

def remove_book():
    if not books: #if list is empty 
        print("No books to remove!\n") #print
        return #return to menu
    view_books()
    try:
        book_number = int(input("Enter the number of the task to remove: ")) #gets user input 
        if 1 <= book_number <= len(books): #valid number has to be greater than or equal to 1(first item) and less than the last  of the list
            removed = books.pop(book_number - 1) #if it valid, remove item from list (-1 since python normally starts at 0)
            print(f"Removed book: {removed}\n") #print
            save_books()
        else:
            print("Invalid book number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def main():
    while True:
        print("=== BOOK LIST MENU ===")
        print("1. View books")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Quit")
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            view_books()
        elif choice == "2":
            add_books()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            print("Goodbye! Your books are saved.")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
