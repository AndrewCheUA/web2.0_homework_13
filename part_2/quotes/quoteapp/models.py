from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=125, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    fullname = models.CharField(max_length=150, null=False, unique=True)
    born_date = models.CharField(max_length=150, null=False)
    born_location = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return f"{self.fullname}"


class Quote(models.Model):
    text = models.TextField(unique=True, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.text}"

    def show_tags(self):
        tag = self.tags.all()
        return tag

    def show_quote_author(self):
        return self.author
