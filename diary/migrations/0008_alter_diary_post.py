# Generated by Django 3.2.9 on 2022-02-15 02:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_diary_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='post',
            field=ckeditor.fields.RichTextField(),
        ),
    ]