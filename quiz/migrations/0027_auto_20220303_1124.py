# Generated by Django 3.2.9 on 2022-03-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0026_auto_20220303_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(default='quiz/images/quiz.jpg', upload_to='quiz/images/'),
        ),
        migrations.AlterField(
            model_name='fourchoicesquestion',
            name='solutionThumbnail',
            field=models.ImageField(default='quiz/images/quiz.jpg', upload_to='quiz/images/'),
        ),
        migrations.AlterField(
            model_name='fourchoicesquestion',
            name='thumbnail',
            field=models.ImageField(default='quiz/images/quiz.jpg', upload_to='quiz/images/'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='picture',
            field=models.ImageField(default='static/quiz/images/quiz.jpg', upload_to='quiz/images/'),
        ),
        migrations.AlterField(
            model_name='trueorfalsequestion',
            name='solutionThumbnail',
            field=models.ImageField(default='quiz/images/quiz.jpg', upload_to='quiz/images/'),
        ),
        migrations.AlterField(
            model_name='trueorfalsequestion',
            name='thumbnail',
            field=models.ImageField(default='quiz/images/quiz.jpg', upload_to='quiz/images/'),
        ),
    ]
