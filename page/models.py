from django.db import models

# Create your models here.


class TestModel(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title