from django.db import models

from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    is_verified = models.BooleanField(default=False)
    verify_code = models.CharField(max_length=20, blank=True, null=True)


    #пришлось переопределить эти поля, без этого проект не стартовал
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user',
    )