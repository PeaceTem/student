# Generated by Django 3.2.9 on 2022-03-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0039_rename_duration_quiz_duration_in_minutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fourchoicesquestion',
            name='solution',
            field=models.TextField(default='The creator of this quiz did not provide any solution for this question!', max_length=500),
        ),
        migrations.AlterField(
            model_name='trueorfalsequestion',
            name='solution',
            field=models.TextField(default='The creator of this quiz did not provide any solution for this question!', max_length=500),
        ),
    ]