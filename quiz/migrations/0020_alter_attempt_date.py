# Generated by Django 3.2.9 on 2022-02-25 01:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0019_alter_attempt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 25, 1, 32, 1, 62992, tzinfo=utc)),
        ),
    ]
