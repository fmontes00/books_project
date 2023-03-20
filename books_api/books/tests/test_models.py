from datetime import date
from freezegun import freeze_time
from django.test import TestCase

from books.tests.fixtures import AuthorFactory, CollaboratorFactory, BookFactory


class TestAuthor(TestCase):
    def setUp(self):
        super().setUp()
        self.author_1 = AuthorFactory(
            name="Jorge Luis Borges", birthday=date(1889, 8, 24)
        )

    def test_author_age(self):
        """Should return the author's age based on his birthday"""
        self.assertEqual(self.author_1.birthday, date(1889, 8, 24))

        with freeze_time("2023-01-01T10:00:00"):
            self.assertEqual(self.author_1.calculate_age, 133)


class TestBook(TestCase):
    def setUp(self):
        super().setUp()
        self.collaborator_1 = CollaboratorFactory(
            name="Juan Perez", profession="Editor"
        )
        self.author_2 = AuthorFactory(
            name="Jorge Luis Borges", birthday=date(1889, 8, 24)
        )
        self.book_1 = BookFactory(
            title="El Aleph", author=self.author_2, publish_date=date(1949, 1, 25)
        )
        self.book_1.collaborators.set([self.collaborator_1])
        # self.book_1.collaborators.add(self.collaborator_1)

    def test_book_title(self):
        """Should return the book's title"""
        self.assertEqual(self.book_1.title, "El Aleph")

    def test_author_name(self):
        """Should return the author's name"""
        self.assertEqual(self.author_2.name, "Jorge Luis Borges")

    def test_collaborator_profession(self):
        """Should return the collaborator's profession"""
        self.assertEqual(self.collaborator_1.profession, "Editor")
