from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def add_to_group(sender, instance, created, **kwargs):
    if instance.job_position == "none":
        none_group = Group.objects.get(name="none")
        none_group.user_set.add(instance)


post_save.connect(add_to_group, sender=CustomUser)


# @receiver(post_save, sender=CustomUser)
# def update_user_group(sender, instance, **kwargs):
#     group_name = instance.job_position
#     try:
#         group = Group.objects.get(name=group_name)
#     except Group.DoesNotExist:
#         group = None
#
#     if group and group not in instance.groups.all():
#         instance.groups.clear()
#         instance.groups.add(group)
