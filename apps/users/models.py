from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=False, null=False)
    phone = PhoneNumberField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'name', 'username']

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_custom_set",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_custom_set",
        blank=True,
        help_text="Specific permissions for this user.",
    )

    class Meta:
         constraints = [
          models.UniqueConstraint(fields=['email'], name='unique_email_user'),
          models.UniqueConstraint(fields=['email', 'phone'], name='unique_email_user_phone'),
         ]
#    indexes = [
#       models.Index(fields=['email', 'phone'])
#  ]
        #ordering = ['created_at', 'id']

# Fix clashes with the default User model
#User._meta.get_field('groups').related_query_name = 'auth_user_groups'
#User._meta.get_field('user_permissions').related_query_name = 'auth_user_user_permissions'
