from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    num_pages = models.IntegerField()
    date_published = models.DateField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

