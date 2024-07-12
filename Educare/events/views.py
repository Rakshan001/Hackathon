from django.shortcuts import render, redirect
from .models import Registration
from students.models import Student
from events.models import Event

def register_event(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        unique_id = request.POST.get('unique_id')
        roll_no = request.POST.get('roll_no')
        class_name = request.POST.get('class_name')
        event_id = request.POST.get('event_id')

        # Assuming event_id is unique for each event, retrieve the Event object
        event = Event.objects.get(event_id=event_id)

        # Create or retrieve the student based on unique_id or roll_no
        student, created = Student.objects.get_or_create(
            unique_id=unique_id,
            defaults={'name': student_name, 'roll_no': roll_no, 'class_name': class_name}
        )

        # Create registration record
        registration = Registration.objects.create(
            student=student,
            event=event
        )

        # Redirect to a success page or another view
        return redirect('registration_success')

    # Render the registration form if the request method is GET
    return render(request, 'events/event_registration.html')
