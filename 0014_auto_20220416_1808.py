# Generated by Django 3.2.9 on 2022-04-16 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
        ('core', '0041_alter_profile_categories'),
        ('question', '0013_auto_20220414_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='FourChoicesQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.CharField(default='fourChoicesQuestion', max_length=30)),
                ('question', models.TextField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('answer1', models.CharField(max_length=200)),
                ('answer2', models.CharField(max_length=200)),
                ('answer3', models.CharField(max_length=200)),
                ('answer4', models.CharField(max_length=200)),
                ('correct', models.CharField(choices=[('answer1', 'answer1'), ('answer2', 'answer2'), ('answer3', 'answer3'), ('answer4', 'answer4')], max_length=100)),
                ('solution', models.TextField(default='The creator of this quiz did not provide any solution for this question!', max_length=500)),
                ('duration_in_seconds', models.PositiveSmallIntegerField(choices=[(15, 15), (20, 20), (25, 25), (30, 30), (35, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60), (65, 65), (70, 70), (75, 75), (80, 80), (85, 85), (90, 90), (95, 95), (100, 100), (105, 105), (110, 110), (115, 115), (120, 120), (125, 125), (130, 130), (135, 135), (140, 140), (145, 145), (150, 150), (155, 155), (160, 160), (165, 165), (170, 170), (175, 175), (180, 180)], default=15)),
                ('attempts', models.PositiveIntegerField(default=0)),
                ('avgScore', models.FloatField(default=0.0)),
                ('solution_quality', models.IntegerField(default=0)),
                ('answer1NumberOfTimesTaken', models.PositiveIntegerField(default=0)),
                ('answer2NumberOfTimesTaken', models.PositiveIntegerField(default=0)),
                ('answer3NumberOfTimesTaken', models.PositiveIntegerField(default=0)),
                ('answer4NumberOfTimesTaken', models.PositiveIntegerField(default=0)),
                ('shuffleAnswers', models.BooleanField(default=False)),
                ('standalone', models.BooleanField(default=True, verbose_name='Create as a standalone question too')),
                ('age_from', models.PositiveSmallIntegerField(null=True, verbose_name='Minimum Age Of Quiz Takers')),
                ('age_to', models.PositiveSmallIntegerField(null=True, verbose_name='Maximum Age Of Quiz Takers')),
                ('categories', models.ManyToManyField(blank=True, related_name='FourChoicesQuestioncategories', to='category.Category')),
                ('solution_validators', models.ManyToManyField(blank=True, related_name='fourChoicesQuestion_solution_validators', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrueOrFalseQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.CharField(default='trueOrFalseQuestion', max_length=20)),
                ('question', models.TextField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('answer1', models.CharField(default='True', max_length=20)),
                ('answer2', models.CharField(default='False', max_length=20)),
                ('correct', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=100)),
                ('solution', models.TextField(default='The creator of this quiz did not provide any solution for this question!', max_length=500)),
                ('duration_in_seconds', models.PositiveSmallIntegerField(choices=[(15, 15), (20, 20), (25, 25), (30, 30), (35, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60), (65, 65), (70, 70), (75, 75), (80, 80), (85, 85), (90, 90), (95, 95), (100, 100), (105, 105), (110, 110), (115, 115), (120, 120), (125, 125), (130, 130), (135, 135), (140, 140), (145, 145), (150, 150), (155, 155), (160, 160), (165, 165), (170, 170), (175, 175), (180, 180)], default=20)),
                ('attempts', models.PositiveIntegerField(default=0)),
                ('avgScore', models.FloatField(default=0.0)),
                ('solution_quality', models.IntegerField(default=0)),
                ('answer1NumberOfTimesTaken', models.PositiveIntegerField(default=0)),
                ('answer2NumberOfTimesTaken', models.PositiveIntegerField(default=0)),
                ('standalone', models.BooleanField(default=True, verbose_name='Create as a standalone question too')),
                ('age_from', models.PositiveSmallIntegerField(null=True, verbose_name='Minimum Age Of Quiz Takers')),
                ('age_to', models.PositiveSmallIntegerField(null=True, verbose_name='Maximum Age Of Quiz Takers')),
                ('categories', models.ManyToManyField(blank=True, related_name='trueOrFalseQuestioncategories', to='category.Category')),
                ('solution_validators', models.ManyToManyField(blank=True, related_name='trueOrFalse_solution_validators', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='qtrueorfalsequestion',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='qtrueorfalsequestion',
            name='solution_validators',
        ),
        migrations.RemoveField(
            model_name='qtrueorfalsequestion',
            name='user',
        ),
        migrations.DeleteModel(
            name='QFourChoicesQuestion',
        ),
        migrations.DeleteModel(
            name='QTrueOrFalseQuestion',
        ),
    ]