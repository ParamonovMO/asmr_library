import pytest
from book import Book


class TestBook:

    @pytest.mark.parametrize('title, author', [('Одиссея', 'Гомер'), ('Война и мир', 'Лев Толстой'), ('Гамлет', 'Уильям Шекспир')])
    def test_init(self,  title, author):
        books = Book(title, author)
        assert books.title == title and books.author == author

    @pytest.mark.parametrize('title, author', [('Одиссея', 'Гомер'), ('Война и мир', 'Лев Толстой'), ('Гамлет', 'Уильям Шекспир')])
    def test_str(self, title, author):
        books = Book(title, author)
        assert books.__str__() == f'Название книги: {title}, автор книги: {author}'

    @pytest.mark.parametrize('title, author', [('Одиссея', 'Гомер'), ('Война и мир', 'Лев Толстой'), ('Гамлет', 'Уильям Шекспир')])
    def test_repr(self, title, author):
        books = Book(title, author)
        assert books.__repr__() == f'{title}, {author}'
