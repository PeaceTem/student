# Generated by Django 3.2.9 on 2022-04-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0011_auto_20220407_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='qfourchoicesquestion',
            name='shuffleAnswers',
            field=models.BooleanField(default=False),
        ),
    ]
