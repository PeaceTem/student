# Generated by Django 3.2.9 on 2022-04-02 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0044_quiz_solution_validators'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='likeCount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]