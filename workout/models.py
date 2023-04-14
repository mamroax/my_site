from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from food.models import Diet
from django.utils import timezone


class Workout_exercises(models.Model):
    video = models.TextField()
    instructions = models.TextField()
    workout_aim = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='exercise_pics')
    intensity = models.IntegerField()
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super(Workout_exercises, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Workout_program(models.Model):
    exercises_id = models.ForeignKey(Workout_exercises, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=100)
    intensity = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    workout_aim = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()


class Physical_form(models.Model):
    """Это связующий класс для всех сущностей,
     хранящихся в БД(диета и еда, пользователи и посты в блоге"""
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    weight = models.FloatField()
    intensity = models.IntegerField()
    workout_id = models.ForeignKey(Workout_program, on_delete=models.CASCADE)
    diet_id = models.ForeignKey(Diet, on_delete=models.CASCADE)
    workout_aim = models.CharField(max_length=100)
    muscles = models.FloatField()
    fat = models.FloatField()
    body_type = models.TextField()
