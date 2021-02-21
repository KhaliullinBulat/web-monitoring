from django.db import models
from account.models import Account


class Link(models.Model):
    name = models.CharField(max_length=120, blank=True)
    link = models.CharField(max_length=1000)
    finish_link = models.CharField(max_length=1000, default='')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='links', blank=True, null=True)
    response = models.IntegerField(blank=True, default=0)
    resp_text = models.CharField(max_length=100000000, blank=True, default='')
    last_check_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, blank=True)
    error = models.CharField(max_length=1000, blank=True)
    in_schedule = models.BooleanField(default=False)

    def __str__(self):
        return self.name
