from django.urls import path
from . import views

urlpatterns = [
    # path('enter_marks/', views.enter_marks, name='enter_marks'),
    # path('view_marks/', views.view_marks, name='view_marks'),
    # path('top_students/', views.top_students, name='top_students'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('student_performance_chart/', views.student_performance_chart, name='student_performance_chart'),
    # Add other URL patterns as needed
]
