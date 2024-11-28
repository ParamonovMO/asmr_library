from book import Book
from library import Library
from user import User


if __name__ == '__main__':
    book = Book('Гамлет', 'Уильям Шекспир')
    book_2 = Book('Война и мир', 'Лев Толстой')

    user = User('Максим', 'Парамонов')

    library = Library()
    library.add_book_to_library(book)
    library.add_book_to_library(book_2)

    print(library)
    print(library.get_books_by_library())
    library.issue_book(user, book_2)

    print(user.get_user_books())

    print(library.get_books_by_library())

    print(library.get_issue_books())
