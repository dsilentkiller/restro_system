from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


# Create your models here.
Role_Choices = (('waiter', 'waiter'),
                ('accountant', 'accountant'),
                ('chef', 'chef'),
                ('staff', 'staff'),)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_active=True, **extra_fields):
        email = UserManager.normalize_email(email)
        extra_fields.pop('username', None)

        user = self.model(email=email, is_active=is_active,
                          is_staff=is_staff, **extra_fields)

        if password:
            user.set_password(password)
        user.save()
        return user
