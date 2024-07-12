from django.db import models
from students.models import Student

class Batch(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return f"{self.start_year}-{self.end_year}"

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} ({self.batch})"

class Marks(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    ia1_marks = models.IntegerField(null=True, blank=True, default=None)
    ia2_marks = models.IntegerField(null=True, blank=True, default=None)
    ia3_marks = models.IntegerField(null=True, blank=True, default=None)
    midterm_marks = models.IntegerField(null=True, blank=True, default=None)
    final_marks = models.IntegerField(null=True, blank=True, default=None)
    total = models.IntegerField(editable=False, null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        self.total = (self.ia1_marks or 0) + (self.ia2_marks or 0) + (self.ia3_marks or 0) + (self.midterm_marks or 0) + (self.final_marks or 0)
        super(Marks, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.enrollment.student.name} - {self.enrollment.subject.name} ({self.enrollment.batch})"











from django.db import models
from students.models import Student

class Achievement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    date = models.DateField()
    outcome = models.TextField()
    photo = models.ImageField(upload_to='achievement_photos/', blank=True, null=True)

    def __str__(self):
        return f"Achievement for {self.student.name}: {self.event}"

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'
