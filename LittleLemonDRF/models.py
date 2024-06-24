from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    rating = models.SmallIntegerField()
    menuitem_id = models.SmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)