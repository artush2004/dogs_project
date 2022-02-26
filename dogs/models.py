from django.db import models
from django.urls import reverse

class Dog(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dog_detail', args=[str(self.id)])