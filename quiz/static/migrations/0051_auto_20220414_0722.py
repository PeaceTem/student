# Generated by Django 3.2.9 on 2022-04-14 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0050_auto_20220411_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fourchoicesquestion',
            old_name='question_text',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='trueorfalsequestion',
            old_name='question_text',
            new_name='question',
        ),
    ]
