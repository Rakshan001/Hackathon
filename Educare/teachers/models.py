from django.db import models
from students.models import Student, School

class Batch(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.school.name} ({self.start_year}-{self.end_year})"

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubjectGroup(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f"Subject Group for {self.batch}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    subject_group = models.ForeignKey(SubjectGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.subject_group} ({self.batch})"

class Marks(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    ia1_marks = models.IntegerField(null=True, blank=True, default=None)
    ia2_marks = models.IntegerField(null=True, blank=True, default=None)
    ia3_marks = models.IntegerField(null=True, blank=True, default=None)
    midterm_marks = models.IntegerField(null=True, blank=True, default=None)
    final_marks = models.IntegerField(null=True, blank=True, default=None)
    total = models.IntegerField(editable=False, null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        self.total = (self.ia1_marks or 0) + (self.ia2_marks or 0) + (self.ia3_marks or 0) + (self.midterm_marks or 0) + (self.final_marks or 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.enrollment.student.name} - {self.subject.name} ({self.enrollment.batch})"
