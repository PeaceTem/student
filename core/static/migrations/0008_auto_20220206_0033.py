# Generated by Django 3.2.9 on 2022-02-05 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220206_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='diaries',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='quizAttempted',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='quizCreated',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='tasks',
        ),
    ]
