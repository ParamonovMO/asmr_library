class Library:
    count_books = 0

    def __init__(self, name):
        self.name = name
        self.library = {}
        self.id_book = Library.count_books
        Library.count_books += 1

    def __str__(self) -> str:
        return f'{self.name} владеет следующими книгами: {self.library}'

    def add_book_to_library(self):
        self.title = input('Введите название книги: ')
        self.author = input('Введите автора книги: ')
        self.date_book = int(input('ВВедите год книги: '))
        self.book_info = {self.title, self.author, self.date_book}
        self.library[self.id_book] = self.book_info

    def get_book_by_id(self, id):
        return self.library.get(id)


a = Library('Библиотека')
a.add_book_to_library()
print(a)
print(a.get_book_by_id(0))