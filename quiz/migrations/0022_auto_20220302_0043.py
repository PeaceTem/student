# Generated by Django 3.2.9 on 2022-03-01 23:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0021_alter_attempt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 23, 43, 27, 957209, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ManyToManyField(blank=True, to='quiz.Category'),
        ),
    ]