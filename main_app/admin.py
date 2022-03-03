from django.contrib import admin
from .models import Plant, Watering, Fertilizer, Photo

# Register your models here.

admin.site.register(Plant)
admin.site.register(Watering)
admin.site.register(Fertilizer)
admin.site.register(Photo)
