from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Fertilizer(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand} {self.name}"
    
    def get_absolute_url(self):
        return reverse('fertilizer_detail', kwargs={'pk': self.id})

class Plant(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    fertilizers = models.ManyToManyField(Fertilizer)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

class Watering(models.Model):
    date = models.DateField('Watering date')
    fertilized = models.BooleanField('Fertilized?')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        if self.fertilized == True:
            return f"Fertilized and watered on {self.date}"
        else:
            return f"Watered on {self.date}"
    class Meta:
        ordering = ('-date',)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for plant_id: {self.plant_id} @{self.url}"