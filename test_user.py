class TestUser:

    def test_init(self, user):
        assert user.name == 'Максим'
        assert user.last_name == 'Парамонов'
        assert len(user.books) == 0

    def test_add_books(self, user, book):
        user.add_books(book)
        assert len(user.books) == 1

    def test_get_books(self, user, book):
        user.add_books(book)
        assert len(user.get_user_books()) == 1

    def test_issue_book(self, user, book):
        user.add_books(book)
        user.issue_book(book)
        assert len(user.get_user_books()) == 0

    def test_str(self, user):
        assert user.__str__() == f'{user.name, user.last_name, user.books}'

    def test_repr(self, user):
        assert user.__repr__() == f'{user.name, user.last_name, user.books}'
