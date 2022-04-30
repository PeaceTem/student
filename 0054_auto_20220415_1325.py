# Generated by Django 3.2.9 on 2022-04-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0053_attempter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attempter',
            options={'ordering': ['-percentage', '-score']},
        ),
        migrations.AlterField(
            model_name='quiz',
            name='age_from',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Minimum Age Of Quiz Takers'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='age_to',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Maximum Age Of Quiz Takers'),
        ),
    ]