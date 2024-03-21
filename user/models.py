from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


# Create your models here.
Role_Choices = (('waiter', 'waiter'),
                ('accountant', 'accountant'),
                ('chef', 'chef'),
                ('staff', 'staff'))


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

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields)
        return user


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=8)
    role = models.CharField(choices=Role_Choices, max_length=200)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = ('email')
    objects = UserManager()

    def has_permission(self, perm, obj=None):
        'Does the user have a specific permission?'
        return True  # does the user has specific permission if so return true

    # def is_staff(self):
    #     'Is the user a member of staff??'
    #     return self.staff

    def is_admin(self):
        'Is the user a admin member?'
        return self.admin

    def _str__(self):
        return self.email
