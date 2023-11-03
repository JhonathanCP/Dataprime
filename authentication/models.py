from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model
from django.db import models

from core.models import Clasificacion

class CustomUser(AbstractUser):
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (USER, 'User'),
        (GUEST, 'Guest'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)
    clasificaciones = models.ManyToManyField(Clasificacion, blank=True)

    # Agregar related_name para evitar conflictos con los campos groups y user_permissions
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_users')

class UserActivity(models.Model):
    user = models.ForeignKey(CustomUser(), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
    details = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.action} at {self.timestamp}"
