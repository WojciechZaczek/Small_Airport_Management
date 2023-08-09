from django.db.models.signals import post_save
from .models import CustomUser, Worker
from django.dispatch import receiver


@receiver(post_save, sender=CustomUser)
def create_worker(sender, instance, created, **kwargs):
    if created:
        Worker.objects.create(worker=instance)


@receiver(post_save, sender=CustomUser)
def save_worker(sender, instance, **kwargs):
    instance.worker.save()
