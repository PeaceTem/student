# Generated by Django 3.2.9 on 2022-01-25 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_alter_diary_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='post',
            field=models.TextField(),
        ),
    ]