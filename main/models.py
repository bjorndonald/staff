from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    staff_name= models.CharField(max_length=800)
    date_of_birth=models.DateField(max_length=800)
    date_of_first_appointment=models.DateField(max_length=800)

    class Meta:
        verbose_name_plural = 'staff'
    def __str__(self):
        return self.staff_name