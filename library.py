class Library:
    count_books = 0

    def __init__(self):
        self.name = 'Библиотека'
        self.dict_library = {}
        self.issue = []

    def get_books_by_library(self):
        return self.dict_library

    def add_book_to_library(self, book):
        self.dict_library[Library.count_books] = book
        Library.count_books += 1

    def issue_book(self, user, book):
        for k, v in list(self.dict_library.items()):
            if v == book:
                user.books.append(book)
                print(f'Название: {self.dict_library.get(k)} выдана {user.name, user.last_name}')
                self.issue.append(self.dict_library[k])
                del self.dict_library[k]
                Library.count_books -= 1
        return 'Такой книги нет в библиотеке'

    def get_issue_books(self):
        return self.issue
