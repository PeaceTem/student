# Generated by Django 3.2.9 on 2022-04-14 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0012_qfourchoicesquestion_shuffleanswers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qfourchoicesquestion',
            old_name='question_text',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='qtrueorfalsequestion',
            old_name='question_text',
            new_name='question',
        ),
    ]
