from django.contrib import admin
from .models import Workout_program, Workout_exercises, Physical_form
# Register your models here.
admin.site.register(Workout_exercises)
admin.site.register(Workout_program)
admin.site.register(Physical_form)
