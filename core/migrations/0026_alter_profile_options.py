# Generated by Django 3.2.9 on 2022-03-18 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_profile_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-coins']},
        ),
    ]
