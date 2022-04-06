from __future__ import absolute_import, unicode_literals

from celery import shared_task

@shared_task
def add(x: int , y: int):
    return x + y


# celery -A student worker -l info
# add.apply async{(3,3), countdown=5}