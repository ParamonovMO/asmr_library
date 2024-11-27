from book import Book
from library import Library

if __name__ == '__main__':
    book = Book('У Лукоморья', 'Пушкин')
    book_2 = Book('Война и мир', 'Толстой')

    library = Library()
    library.add_book_to_library(book)
    library.add_book_to_library(book_2)

    print(library.get_books_by_library())
    library.issue_book(book_2)

    print(library.get_books_by_library())

    print(library.get_issue_books())
