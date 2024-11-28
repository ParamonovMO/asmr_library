import pytest
from book import Book
from library import Library
from user import User


@pytest.fixture
def book():
    return Book('Война и мир', 'Лев Толстой')


@pytest.fixture
def library():
    return Library()


@pytest.fixture
def user():
    return User('Максим', 'Парамонов')
