# Generated by Django 3.2.9 on 2022-02-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_auto_20220205_1828'),
        ('core', '0005_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='coins',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='quizAttempted',
        ),
        migrations.AddField(
            model_name='profile',
            name='quizAttempted',
            field=models.ManyToManyField(related_name='quiz_attempted', to='quiz.Quizzes'),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='quizCreated',
        ),
        migrations.AddField(
            model_name='profile',
            name='quizCreated',
            field=models.ManyToManyField(related_name='quiz_created', to='quiz.Quizzes'),
        ),
    ]