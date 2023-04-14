from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.utils import timezone

class Food(models.Model):
    food_name = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.FloatField()
    fat = models.FloatField()
    proteins = models.FloatField()
    carbohydrates = models.FloatField()
    glycemic_index = models.FloatField()
    food_image = models.ImageField(default='default.jpg', upload_to='food_pics')

    def __str__(self):
        return f'{self.food_name} food'

    def get_absolute_url(self):
        return reverse('food-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Food, self).save(*args, **kwargs)

        img = Image.open(self.food_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.food_image.path)

class Diet(models.Model):
    food_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    diet_name = models.CharField(max_length=100)
    schedule = models.DateTimeField(default=timezone.now)
    calories = models.FloatField()
    glycemic_index = models.FloatField()
    diet_aim = models.CharField(max_length=100)
