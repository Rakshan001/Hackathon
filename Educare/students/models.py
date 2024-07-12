from django.db import models
from django.contrib.auth.models import User
import random
import string

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=6, unique=True, editable=False)
    name = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=50, unique=True)
    student_class = models.CharField(max_length=50)
    current_school = models.ForeignKey(School, related_name='current_students', on_delete=models.SET_NULL, null=True)
    fathers_name= models.CharField(max_length=255)
    mothers_name = models.CharField(max_length=255)

    parents_phone_number = models.CharField(max_length=15)
    student_phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    interests = models.TextField()
    photo = models.ImageField(upload_to='students/students_profile_imges/', blank=True, null=True,default="")

    def __str__(self):
        return f"{self.name} ({self.unique_id})"

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.generate_unique_id()
        super().save(*args, **kwargs)

    def generate_unique_id(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class SchoolHistory(models.Model):
    student = models.ForeignKey(Student, related_name='school_history', on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.school.name} ({self.start_date} to {self.end_date})"



class Achievement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    date = models.DateField()
    outcome = models.TextField()
    photo = models.ImageField(upload_to='students/achievement_photos/', blank=True, null=True)

    def __str__(self):
        return f"Achievement for {self.student.name}: {self.event}"

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'
