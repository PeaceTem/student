# Generated by Django 3.2.9 on 2022-03-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0040_auto_20220327_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trueorfalsequestion',
            name='question_text',
            field=models.TextField(max_length=500),
        ),
    ]