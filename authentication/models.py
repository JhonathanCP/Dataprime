from django.contrib.auth.models import AbstractUser
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

class UserActivity(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)  # Por ejemplo, "Login", "Page visit", etc.
    details = models.CharField(max_length=200, blank=True, null=True)  # Puede ser una URL o descripción adicional

    def __str__(self):
        return f"{self.user} - {self.action} at {self.timestamp}"