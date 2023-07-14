from pprint import pprint

### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

# def read_books(library):

#     new_list = []

#     with open(library, "r") as f:
#         file = f.readlines()


#         for line in file:

#             title, author, year, rating, pages = line.split(", ")

#             new_list.append ({
#                 "title": title,
#                 "author": author,
#                 "year": int(year),
#                 "rating": float(rating),
#                 "pages": int(pages)
#             })

#     pprint(new_list) 

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def return_dictionary_list(library):

    new_list = []

    with open(library, "r") as f:
        file = f.readlines()


        for line in file:

            title, author, year, rating, pages = line.split(", ")

            new_list.append ({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })

    return new_list
    
def new_book(library):

    title = input("What is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")

    try:
        year = int(input("What year was this book published? - "))
    except:
        year = int(input("Please type an integer for the year - "))

    try:
        rating = float(input("What rating out of 5 would you give this book? - "))
    except:
        rating = float(input("Please type the rating using numbers. - "))

    try:
        pages = int(input("What is the page count of the book? - "))
    except:
        pages = int(input("Please type an integer for the page count. - "))

    with open(library, "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")


    for book in return_dictionary_list(library):
        pprint(book)

def library_reader(library):
    for book in return_dictionary_list(library):
        print(book)

def find_by_genre(library, genre):
    for book in library:
        if book['genre'] == genre:
            print(f"{book['title']}")

def find_by_minRating(library, rating):
    for book in library:
        if book['rating'] >= rating:
            print(f"{book['title']}")

def menu(library):

    power_on = True

    while power_on:
        option = input("""
        
            Welcome!
            Type 1 to browse our shelves.
            Type 2 to donate a book.
            Type 3 to exit.
                       
                       """)
        

        if option == "1":
            print('Please enjoy our selection.')
            pprint(return_dictionary_list(library))

        elif option == "2":
            new_book(library)
            print("Thank you for your donation!")

        elif option == "3":
                return
        else:
            print("Please select an option.")

if __name__ == "__main__":
    menu("library.txt")



