# Generated by Django 3.2.9 on 2022-03-18 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0035_quiztaker'),
        ('question', '0002_auto_20220312_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='qfourchoicesquestion',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='FourChoicesQuestioncategories', to='quiz.Category'),
        ),
        migrations.AddField(
            model_name='qtrueorfalsequestion',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='trueOrFalseQuestioncategories', to='quiz.Category'),
        ),
    ]
