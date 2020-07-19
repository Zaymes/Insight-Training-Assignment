from django.db import models

# Create your models here.


class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()


    def __str__(self):
        return self.name


class BlogPost(BaseClass):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title
