# dictionary of books with authors 
books = {"The Handmaids Tale":"Margaret Attwood", 
         "The Hobbit":"J.R.R. Tolkien", 
         "Charlie and the Chocolate Factory":"Roald Dahl", 
         "The Last Wish":"Andrzej Sapkowski", 
         "Sword of Destiny":"Andrzej Sapkowski",
         "Blood of Elves": "Andrzej Sapkowski", 
         "The Time of Contempt":"Andrzej Sapkowski"}

# ask for authors name
booksvar = input("Please insert authors name: ")
# empty list to store books by author 
booksByAuthor = []

# check if author is in dictionary 
if booksvar not in books.values():
    print("No books by", booksvar, "in the list")
else:
    print("The following books are written by", booksvar + ":")
# loop through books in dictionary 
    for book in books: 
        # check if the author of the book is the same as entered by user
        if books[book] == booksvar:
            # add book to the list of books by author 
            booksByAuthor.append(book)
        # sort the list of books alphabetically 
        booksByAuthor = sorted(booksByAuthor)
        # print the list of books 
        print(', '.join(booksByAuthor))
