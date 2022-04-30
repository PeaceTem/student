# Generated by Django 3.2.9 on 2022-04-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('core', '0040_profile_favoritequizzes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='profileCategories', to='category.Category'),
        ),
    ]
