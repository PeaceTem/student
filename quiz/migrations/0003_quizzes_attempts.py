# Generated by Django 3.2.9 on 2021-12-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20211222_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizzes',
            name='attempts',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
