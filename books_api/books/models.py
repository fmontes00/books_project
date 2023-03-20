from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel
import uuid
from datetime import date


class UUIDModelMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class BaseModel(TimeStampedModel, UUIDModelMixin):
    class Meta:
        abstract = True


class Author(BaseModel):
    name = models.CharField(max_length=1000)
    biography = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)

    @property
    def calculate_age(self):
        today = date.today()
        return (
            today.year
            - self.birthday.year
            - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        )

    def __str__(self):
        return f"{self.name}"


class Collaborator(BaseModel):
    EDITOR = "editor"
    PROOFREADER = "proofreader"
    GRAPHIC_DESIGNER = "graphic designer"
    ILLUSTRATOR = "ilustrator"
    PUBLICIST = "publicist"

    collaborator_profession_choices = [
        (EDITOR, "Editor"),
        (PROOFREADER, "Proofreader"),
        (GRAPHIC_DESIGNER, "Graphic Designer"),
        (ILLUSTRATOR, "Ilustrator"),
        (PUBLICIST, "Publicist"),
    ]

    name = models.CharField(max_length=1000)
    profession = models.CharField(
        max_length=100, choices=collaborator_profession_choices, blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"


class Book(BaseModel):
    author = models.ForeignKey(
        "books.Author", on_delete=models.CASCADE, related_name="books"
    )
    collaborators = models.ManyToManyField(
        "books.Collaborator", blank=True, related_name="books"
    )
    title = models.CharField(max_length=1500)
    publish_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
