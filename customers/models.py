from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=20, unique=True)
    photo = models.ImageField(upload_to='customer_photos/', null=True,
                              blank=True)
    created_by = models.ForeignKey(User, related_name='created_customers',
                                   on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey(User, related_name='modified_customers',
                                    on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname} (ID: {self.customer_id})"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
