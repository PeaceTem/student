# Generated by Django 3.2.9 on 2022-03-06 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0030_auto_20220303_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='releasedDate',
        ),
    ]
