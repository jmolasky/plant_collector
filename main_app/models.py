from django.db import models
from django.urls import reverse

# Create your models here.

# FEEDINGS = (
#     ('N', 'No'),
#     ('Y', "Yes"),
# )

class Plant(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

class Watering(models.Model):
    date = models.DateField('Watering date')
    # fertilized = models.CharField(max_length=1, choices=FEEDINGS, default=FEEDINGS[0][0])
    fertilized = models.BooleanField('Fertilized?')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        if self.fertilized == True:
            return f"Fertilized and watered on {self.date}"
        else:
            return f"Watered on {self.date}"
    class Meta:
        ordering = ('-date',)