# Generated by Django 3.2.9 on 2022-04-06 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0009_auto_20220403_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='qfourchoicesquestion',
            name='answer1NumberOfTimesTaken',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qfourchoicesquestion',
            name='answer2NumberOfTimesTaken',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qfourchoicesquestion',
            name='answer3NumberOfTimesTaken',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qfourchoicesquestion',
            name='answer4NumberOfTimesTaken',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qtrueorfalsequestion',
            name='answer1NumberOfTimesTaken',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qtrueorfalsequestion',
            name='answer2NumberOfTimesTaken',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
