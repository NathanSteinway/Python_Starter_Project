my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

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

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def bookFunction(my_book):
    book_string = f"{my_book['title']}, written by {my_book['author']} in {my_book['year']}, is {my_book['pages']} pages long with a rating of {my_book['rating']}"
    return book_string

print(bookFunction(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def bookTitle(my_book):
    book_string = f"{my_book['title']}"
    return book_string

print(bookTitle(my_book))

def bookAuthor(my_book):
    book_string = f"{my_book['author']}"
    return book_string

print (bookAuthor(my_book))

def bookYear(my_book):
    book_string = f"{my_book['year']}"
    return book_string

print(bookYear(my_book))

def bookPages(my_book):
    book_string = f"{my_book['pages']}"
    return book_string

print(bookPages(my_book))

def bookRating(my_book):
    book_string = f"{my_book['rating']}"
    return book_string

print(bookRating(my_book))


# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

# print library contents

def library_reader(library):
    for book in library:
        print(book)

library_reader(library)

# print books w/ matching genre

def find_by_genre(library, genre):
    for book in library:
        if book['genre'] == genre:
            print(f"{book['title']}")

find_by_genre(library, 'Mythology')

def find_by_minRating(library, rating):
    for book in library:
        if book['rating'] >= rating:
            print(f"{book['title']}")
    
find_by_minRating(library, 4)