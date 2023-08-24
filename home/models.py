from django.db import models

class Contact(models.Model):

    email = models.EmailField(blank=True, null=True)

    message = models.TextField()

    phone_number = models.CharField(max_length=10, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
