from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)  # дата создания

    def __str__(self):
        return self.title