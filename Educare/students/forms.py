from django import forms
from .models import Student

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name', 'roll_no', 'student_class', 'current_school',
            'fathers_name', 'mothers_name', 'parents_phone_number',
            'student_phone_number', 'email', 'interests', 'photo'
        ]
