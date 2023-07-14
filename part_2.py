### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = [ 'Motohisa Yamakage', 'Joseph Conrad', 'John Gardner', 'Homer', 'Fyodor Dostoevsky', 'Oscar Wilde', 'Khaled Hosseini', 'J. R. R. Tolkein', 'Harper Lee', 'J.D. Salinger' ]

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here

my_authors.append('Ernest Hemmingway')
# Example: my_authors.append("H.G. Wells")
print(my_authors)


# Now let's remove an element in the list

my_authors.remove('Joseph Conrad')
# Example: my_authors.remove("H.G. Wells")
print(my_authors)

# Now access an element by it's index. (Remember it indexes start at 0.)

my_authors[4]
print(my_authors[4])
# Example: my_authors[2]


# Now slice the list.

my_authors[0:1]
# Example: my_authors[1:4]

print(my_authors[0:1])


### Step 2 - Tuples ###

print('---------------------------------------------------------------------------------------------------------')

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

fav_poets_tuple = ( 'e. e. cummings', 'Robert Frost', 'Edgar Allen Poe', 'Langston Hughes', 'Shel Silverstein', 'Mary Oliver' )
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")

print(fav_poets_tuple)
### Step 3 - Sets ###

# Create a set with your authors.

foreign_authors_set = { 'Alexander Solzhenitsyn', 'Vladimir Nabokov', 'Anton Chekhov' }
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


# Add a new author to your set.

foreign_authors_set.add('Friedrich Nietzsche')
# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.

foreign_authors_set.add('Friedrich Nietzsche')
print(foreign_authors_set)
# Example: my_author_set.add("J.R.R. Tolkien")


### Step 4 - For Loops ###
print('---------------------------------------------------------------------------------------------------------')

# Create a for-loop for each of the data-structures above.

for author in my_authors:
    print([author])

for poet in fav_poets_tuple:
    print((poet))

for foreign_author in foreign_authors_set:
    print(foreign_author)

# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

