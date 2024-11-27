class Library:
    count_books = 0

    def __init__(self):
        self.name = 'Библиотека'
        self.library = {}
        self.issue = []

    def __str__(self):
        for k, v in self.library:
            return str(f'{str(k), str(v)}')

    def get_books_by_library(self):
        return self.library

    def add_book_to_library(self, book):
        self.library[Library.count_books] = book
        Library.count_books += 1

    def issue_book(self, book):
        for k, v in list(self.library.items()):
            if v == book:
                print(f'Название: {self.library.get(k)} выдана')
                self.issue.append(self.library[k])
                del self.library[k]

    def get_issue_books(self):
        return self.issue
