class Book:
    def __init__(self, title, autor):
        self.title = title
        self.author = autor

    def __repr__(self):
        return f'{self.title}, {self.author}'

    def __str__(self):
        return f'{self.title}, автор книги: {self.author}'
