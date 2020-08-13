from django.db import models


class ApiSecretToken(models.Model):
    api_name = models.CharField(max_length=50)
    is_web_client = models.BooleanField(default=False)
    api_key = models.CharField(max_length=50, blank=True)

