# Generated by Django 3.2.9 on 2022-03-03 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0024_auto_20220302_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quiz',
            name='releasedDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]