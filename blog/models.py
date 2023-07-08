from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length= 15, blank=True)
    body = models.TextField(blank=True)
    autor = models.CharField(max_length= 15, blank=True)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
