
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import QuizComment, Comment

from quiz.models import Quiz

"""
Whenever a user is created, loop through the sessionstore
"""


@receiver(post_save, sender=Quiz)
def create_quiz_comment(sender, instance, created, *args, **kwargs):
    if created:
        QuizComment.objects.create(quiz=instance)




# @receiver(post_save, sender=Quiz)
# def update_quiz_comment(sender, instance, created, *args, **kwargs):
#     if not created:
#         if not instance.quizComment:
#             instance.QuizComment.create(quiz=instance)
