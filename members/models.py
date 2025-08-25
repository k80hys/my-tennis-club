from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)
    joined_date = models.DateField(null=True)

# Create your models here.
