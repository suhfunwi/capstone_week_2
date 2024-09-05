class Author:
    def __init__(self, name):
        self.name = name
        self.books = []
        # self.books is an empty list so don't need a books argument

    def publish(self, title):
        self.books.append(title)
    # make a new method to publish the books
    # takes a title argument and adds it to self.books

    def __str__(self):
        if self.books:
            book_list = ', '.join(self.books)
            # use join to add the list of books to the string method
        else:
            book_list = 'No books published'
        #     if there aren't any books for the author
        return f'Name: {self.name}. Books published: {book_list}'
#     good to use string formatting when concatenating things


def main():
    shakespeare = Author('William Shakespeare')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Macbeth')
    shakespeare.publish('Hamlet')
    print(shakespeare.name)
    print(shakespeare.books)
    print(shakespeare)
    suh = Author('Suh')
    print(suh)

    books_no_duplicates = list(set(shakespeare.books))
    print(books_no_duplicates)
# turn the list into a set and back in to a list to weed out duplicates.
# not very sure how to go about the syntax for the error message though


main()
