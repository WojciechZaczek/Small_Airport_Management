from django.db import models
from django.utils import timezone
from users.models import CustomUser


class Notification(models.Model):
    title = models.CharField(max_length=100, help_text="Notification title")
    content = models.TextField(help_text="Main information ")
    date_posted = models.DateTimeField(default=timezone.now(), help_text="Date post")
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, help_text="Author of notification"
    )
    view_date = models.DateField(
        help_text="date when notification will appear on dashboard"
    )

    def __str__(self):
        return self.title
