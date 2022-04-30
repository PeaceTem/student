# Generated by Django 3.2.9 on 2022-04-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0052_auto_20220414_1553'),
        ('core', '0039_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favoriteQuizzes',
            field=models.ManyToManyField(blank=True, related_name='favoriteQuizzes', to='quiz.Quiz'),
        ),
    ]
