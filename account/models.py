from django.db import models
from django.conf import settings


class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # def __str__(self):
    #     try:
    #         return self.user.name
    #     except Exception():
    #         return self.user_id
