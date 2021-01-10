from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=300)
    amount = models.IntegerField()

    def __str__(self):
        return self.title