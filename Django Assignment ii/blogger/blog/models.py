from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class BaseClass(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(BaseClass,self).save(*args,**kwargs)

    class Meta:
        abstract = True



class Blog(BaseClass):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title




