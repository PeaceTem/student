# Generated by Django 3.2.9 on 2022-03-23 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20220322_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='relevance',
            new_name='likes',
        ),
        migrations.AddField(
            model_name='profile',
            name='quizzes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='coins',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=200),
        ),
    ]
