class TestLibrary:

    def test_init(self, library):
        assert library.name == 'Библиотека'
        assert len(library.dict_library) == 0
        assert len(library.issue) == 0

    def test_add_book_to_library(self, library, book):
        library.add_book_to_library(book)
        assert len(library.dict_library) == 1

    def test_get_books_by_library_not_add_book(self, library):
        assert library.get_books_by_library() == {}

    def test_get_books_by_library(self, library, book):
        library.add_book_to_library(book)
        assert library.get_books_by_library != {}

    def test_issue_book(self, library, user, book):
        library.add_book_to_library(book)
        library.issue_book(user, book)
        assert library.dict_library == {} and len(library.issue) == 1

    def test_issue_not_book(self, library, user, book):
        library.add_book_to_library(['Война и мир', 'Лев Толстой'])
        library.issue_book(user, book)
        assert 'Такой книги нет в библиотеке'

    def test_get_issue_books(self, library, user, book):
        library.add_book_to_library(book)
        library.issue_book(user, book)
        assert library.get_issue_books() == [book]
