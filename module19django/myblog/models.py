from django.db import models


# Create your models here.

class ReaderPost(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)  # дата создания
    reader_post = models.ManyToManyField(ReaderPost, related_name='myblogs')

    def __str__(self):
        return self.title
