# Generated by Django 4.1.7 on 2023-04-06 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0007_alter_workout_program_intensity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout_program',
            name='reps',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='workout_program',
            name='sets',
            field=models.IntegerField(),
        ),
    ]
