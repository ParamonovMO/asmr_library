class Library:
    count_books = 0

    def __init__(self):
        self.name = 'Библиотека'
        self.library = {}
        self.issue = []

    def __str__(self):
        return ', '.join(str(book) for book in self.library.values())

    def get_books_by_library(self):
        return self.library

    def add_book_to_library(self, book):
        self.library[Library.count_books] = book
        Library.count_books += 1

    def issue_book(self, user, book):
        for k, v in list(self.library.items()):
            if v == book:
                user.books.append(book)
                print(f'Название: {self.library.get(k)} выдана {user.name, user.last_name}')
                self.issue.append(self.library[k])

                del self.library[k]

    def get_issue_books(self):
        return self.issue
