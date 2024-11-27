class User:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.books = []

    def get_user_books(self):
        return self.books

    def add_books(self, book):
        self.books.append(book)

    def issue_book(self, book):
        self.books.remove(book)

    def __str__(self):
        return f'{self.name, self.last_name}'

    def __repr__(self):
        return f'{self.name, self.last_name}'