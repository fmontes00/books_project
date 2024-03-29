import factory
from books.models import Author, Book, Collaborator


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Iterator(
        ["Jorge Luis Borges", "J. K. Rowling", "George R. R. Martin"]
    )
    biography = """Author's biography here ..."""
    birthday = factory.Faker("date_object")


class CollaboratorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Collaborator

    name = factory.Iterator(["Collaborator 1", "Collaborator 2", "Collaborator 3"])
    profession = "Editor"


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    author = factory.SubFactory(AuthorFactory)
    title = factory.Iterator(
        ["El Aleph", "Harry Potter and the sorcerer's stone", "A Game of Thrones"]
    )
    publish_date = factory.Faker("date_object")
