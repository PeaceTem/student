# Generated by Django 3.2.9 on 2022-03-06 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0003_auto_20220306_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='draftquiz',
            name='draft',
        ),
    ]