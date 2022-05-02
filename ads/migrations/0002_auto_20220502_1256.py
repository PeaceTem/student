# Generated by Django 3.2.9 on 2022-05-02 11:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postad',
            name='bannerpageclicks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postad',
            name='bannerpagerelevance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='postad',
            name='bannerpageviews',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postad',
            name='clickers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postad',
            name='correctionpageclicks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postad',
            name='correctionpagerelevance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='postad',
            name='correctionpageviews',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postad',
            name='detailpageclicks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postad',
            name='detailpagerelevance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='postad',
            name='detailpageviews',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postad',
            name='submitpageclicks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postad',
            name='submitpagerelevance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='postad',
            name='submitpageviews',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postad',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
