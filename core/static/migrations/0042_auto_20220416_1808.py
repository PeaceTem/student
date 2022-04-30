# Generated by Django 3.2.9 on 2022-04-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0014_auto_20220416_1808'),
        ('core', '0041_alter_profile_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fourChoicesQuestionsMissed',
            field=models.ManyToManyField(blank=True, related_name='fourChoicesQuestionsMissed', to='question.FourChoicesQuestion'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fourChoicesQuestionsTaken',
            field=models.ManyToManyField(blank=True, related_name='fourChoicesQuestionsTaken', to='question.FourChoicesQuestion'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='trueOrFalseQuestionsMissed',
            field=models.ManyToManyField(blank=True, related_name='trueOrFalseQuestionsMissed', to='question.TrueOrFalseQuestion'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='trueOrFalseQuestionsTaken',
            field=models.ManyToManyField(blank=True, related_name='trueOrFalseQuestionsTaken', to='question.TrueOrFalseQuestion'),
        ),
    ]
