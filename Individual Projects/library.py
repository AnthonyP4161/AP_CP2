#AP 1st Period, Personal Library
library = []
def view():
    print("Books in your library:")
    for i in library:
        print(i)
def add():
    name = input("What is the name of the book: ").title().strip()
    author = input("What is the name of the auther: ").title().strip()
    library.append(f"{name} by {author}")
def remove():
    print("Books in your library:")
    number = 1
    for i in library:
        print(f"{number}. {i}")
        number +=1
    print("Type the number of the book you want to remove")
    placeholder = int(input("Input: "))-1
    print(f"You have removed {library[placeholder]}")
    library.remove(library[placeholder])
def search():
    print("What would you like to search for: ")
    search = input("Input: ").capitalize().strip()
    for i in library:
        if search in i:
            print(i)
def main():
    print("Hiya, welcome to the personal library manager!\nHere you can create a library for all your books.\n\nType the respective number to choose what function you want")
    while True:
        print("1: View\n2: Add\n3: Remove\n4: Search\n5: Exit")
        placeholder = input("Input: ")
        if placeholder == "1":
            view()
        elif placeholder == "2":
            add()
        elif placeholder == "3":
            remove()
        elif placeholder == "4":
            search()
        elif placeholder == "5":
            break
main()