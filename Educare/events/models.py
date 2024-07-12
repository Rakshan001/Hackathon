from django.db import models

class Event(models.Model):
    event_id = models.CharField(max_length=20, unique=True)
    date = models.DateField()
    event_name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    event_type = models.CharField(max_length=100)
    seats = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.event_name




from django.db import models
from students.models import Student
from events.models import Event

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.event.event_name}"
