from django.db import models


class User(models.Model):
    objects = None
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=256)
