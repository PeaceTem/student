# Generated by Django 3.2.9 on 2022-03-03 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0027_auto_20220303_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='picture',
            new_name='thumbnail',
        ),
    ]
