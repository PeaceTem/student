# Generated by Django 3.2.9 on 2022-04-03 02:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0045_quiz_likecount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='solution_validators',
            field=models.ManyToManyField(blank=True, related_name='quiz_solution_validators', to=settings.AUTH_USER_MODEL),
        ),
    ]