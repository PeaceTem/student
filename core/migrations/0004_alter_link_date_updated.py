# Generated by Django 3.2.9 on 2022-04-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_link_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='date_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]