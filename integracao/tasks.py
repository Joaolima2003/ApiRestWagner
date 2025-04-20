from celery import shared_task

@shared_task
def somar(x, y):
    return x + y
