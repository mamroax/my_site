# Generated by Django 4.1.7 on 2023-04-06 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0006_alter_physical_form_age_alter_physical_form_fat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout_program',
            name='intensity',
            field=models.IntegerField(),
        ),
    ]
