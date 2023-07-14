### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

title = input("What is the title of the book you would like to add? - ")
author = input("Who is the author of the book you would like to add? - ")
year = input("What year was this book published? - ")
rating = input("What rating out of 5 would you give this book? - ")
pages = input("What is the page count of the book? - ")

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

def new_book():

    title = input("What is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    year = int(input("What year was this book published? - "))
    rating = float(input("What rating out of 5 would you give this book? - "))
    pages = int(input("What is the page count of the book? - "))



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def new_book():

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


### Step 4 - if/elif/else

library = [
    {
        "title": "Grendel",
        "author": "John Gardner",
        "genre": "Mythology",
        "year": 1971,
        "rating": 5,
        "pages": 174
    },
    {
        "title": "The Essence of Shinto: Japan's Spiritual Heart",
        "author": "Motohisa Yamakage",
        "genre": "Religion",
        "year": 2006,
        "rating": 5,
        "pages": 229
    },
    {
        "title": "Norse Mythology: A Guide to Gods, Heroes, Rituals, and Beliefs",
        "author": "John Lindow",
        "genre": "Mythology",
        "year": 2002,
        "rating": 5,
        "pages": 384
    },
    {
        "title": "Fifty Shades of Grey",
        "author": "E. L. James",
        "genre": "Romance",
        "year": 2011,
        "rating": 1,
        "pages": 514
    }]

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

# Displays all books
def library_reader(library):
    for book in library:
        print(book)

def menu():

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

    converted_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    library.append(converted_dictionary)


    if input("Welcome! Would you like to browse our shelves? Please answer 'yes' or 'no'. ") == 'yes':
        print('Behold!')
        print(library_reader(library))

    elif input("Would you like to donate a book to our library? ") == 'yes':
        new_book()
        print(library)

    else:
        if input("Would you like to leave? Please answer 'yes' or 'no'. ") == 'yes':
            pass
        else:
            menu()
            

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

def menu():

    run = True

    while run == True:

        if input("Welcome! Would you like to browse our shelves? Please answer 'yes' or 'no'. ") == 'yes':
            print('Behold!')
            print(library_reader(library))

        elif input("Would you like to donate a book to our library? ") == 'yes':
            new_book()
            print(library)

        else:
            if input("Would you like to leave? Please answer 'yes' or 'no'. ") == 'yes':
                run = False
                

menu()



