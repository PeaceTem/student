# Generated by Django 3.2.9 on 2022-03-11 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0004_remove_draftquiz_draft'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='draftquiz',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='draftquiz',
            name='fourChoicesQuestions',
        ),
        migrations.RemoveField(
            model_name='draftquiz',
            name='trueOrFalseQuestions',
        ),
        migrations.RemoveField(
            model_name='draftquiz',
            name='user',
        ),
        migrations.RemoveField(
            model_name='drafttrueorfalsequestion',
            name='user',
        ),
        migrations.DeleteModel(
            name='DraftFourChoicesQuestion',
        ),
        migrations.DeleteModel(
            name='DraftQuiz',
        ),
        migrations.DeleteModel(
            name='DraftTrueOrFalseQuestion',
        ),
    ]