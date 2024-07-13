from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Student



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StudentProfileForm
from .models import Student

@login_required
def update_profile(request):
    student = get_object_or_404(Student, user=request.user)
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:student_detail', student_id=student.id)  # Redirect to the detail view of the student
    else:
        form = StudentProfileForm(instance=student)
    return render(request, 'students/update_profile.html', {'form': form})






@login_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id, user=request.user)
    return render(request, 'students/student_detail.html', {'student': student})






# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Student

# @login_required
# def profile(request):
#     student = get_object_or_404(Student, user=request.user)
#     return render(request, 'students/profile.html', {'student': student})

