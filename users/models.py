from django.db import models
from django.contrib.auth.models import User
from django_softdelete.models import SoftDeleteModel

class UserProfile(SoftDeleteModel, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
