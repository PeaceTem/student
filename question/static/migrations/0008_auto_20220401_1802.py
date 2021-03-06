# Generated by Django 3.2.9 on 2022-04-01 17:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0007_alter_qtrueorfalsequestion_question_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='qfourchoicesquestion',
            name='solution_quality',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qfourchoicesquestion',
            name='solution_validators',
            field=models.ManyToManyField(related_name='fourChoicesQuestion_solution_validators', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='qtrueorfalsequestion',
            name='solution_quality',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qtrueorfalsequestion',
            name='solution_validators',
            field=models.ManyToManyField(related_name='trueOrFalse_solution_validators', to=settings.AUTH_USER_MODEL),
        ),
    ]
