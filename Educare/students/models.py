from django.db import models
from django.contrib.auth.models import User
import uuid
import random
import string

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=6, unique=True, editable=False)  # Updated to 6 characters
    name = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=50, unique=True)
    student_class = models.CharField(max_length=50)
    school = models.CharField(max_length=255)
    parents_name = models.CharField(max_length=255)
    parents_phone_number = models.CharField(max_length=15)
    student_phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    interests = models.TextField()
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.unique_id})"

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.generate_unique_id()
        super().save(*args, **kwargs)

    def generate_unique_id(self):
        # Generate a random 6-character alphanumeric ID
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    


