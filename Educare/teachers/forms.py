# from django import forms
# from .models import Marks, Batch, Subject

# class MarksForm(forms.ModelForm):
#     class Meta:
#         model = Marks
#         fields = ['student', 'batch', 'subject', 'ia1_marks', 'ia2_marks', 'ia3_marks', 'midterm_marks', 'final_marks']


from django import forms
from .models import  Batch



class BatchFilterForm(forms.Form):
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(), required=True)
