# Generated by Django 3.2.9 on 2022-03-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0033_auto_20220308_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='categories', related_query_name='categories', to='quiz.Category'),
        ),
    ]