from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Customize the reverse relationship name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='user',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Customize the reverse relationship name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )
    
class Contact(models.Model):
    owner = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    spam = models.BooleanField(default=False)
