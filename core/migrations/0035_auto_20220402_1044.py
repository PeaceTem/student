# Generated by Django 3.2.9 on 2022-04-02 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_rename_useddate_streak_currentdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='url',
            new_name='link',
        ),
        migrations.AlterField(
            model_name='link',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
