from django.db import models
from django.urls import reverse



class Deep(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=30)
    count = models.IntegerField()
    salt = models.CharField(max_length=10, default='salt')
    moon = models.IntegerField(null=True)

    def get_url(self):
        return reverse("deepone", args=[self.id])


    def __str__(self):
        return f'{self.name} - {self.text} - {self.count}'





# Create your models here.
