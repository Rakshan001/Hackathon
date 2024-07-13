# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Marks

# def student_performance_chart(request):
#     # Querying and processing data to generate chart
#     # Example: Grouping by year and calculating average performance
#     data = {
#         'labels': ['Year 1', 'Year 2', 'Year 3', 'Year 4'],
#         'datasets': [
#             {
#                 'label': 'Average Performance',
#                 'data': [80, 75, 85, 90],  # Replace with actual data retrieval logic
#                 'backgroundColor': 'rgba(54, 162, 235, 0.2)',
#                 'borderColor': 'rgba(54, 162, 235, 1)',
#                 'borderWidth': 1,
#             },
#         ]
#     }

#     return JsonResponse(data)









from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from .forms import StudentProfileForm, BatchFilterForm
from .forms import BatchFilterForm
from .models import Student, Marks, Batch

@login_required
def update_profile(request):
    student = get_object_or_404(Student, user=request.user)
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile view after saving
    else:
        form = StudentProfileForm(instance=student)
    return render(request, 'teachers/update_profile.html', {'form': form})

@login_required
def view_marks(request):
    student = get_object_or_404(Student, user=request.user)
    marks = None
    if request.method == 'POST':
        form = BatchFilterForm(request.POST)
        if form.is_valid():
            batch = form.cleaned_data['batch']
            enrollments = student.enrollment_set.filter(batch=batch)
            marks = Marks.objects.filter(enrollment__in=enrollments)
    else:
        form = BatchFilterForm()
    return render(request, 'teachers/view_marks.html', {'form': form, 'marks': marks})
