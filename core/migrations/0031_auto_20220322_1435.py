# Generated by Django 3.2.9 on 2022-03-22 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_profile_relevance'),
    ]

    operations = [
        migrations.CreateModel(
            name='LInk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(blank=True, null=True, unique=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='SessionSecretKey',
        ),
    ]
