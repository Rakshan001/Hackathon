# # students/urls.py
# from django.urls import path
# from . import views

app_name = 'students'

# urlpatterns = [
#     path('update/<int:student_id>/', views.update_student, name='update_student'),
#     path('detail/<int:student_id>/', views.student_detail, name='student_detail'),
# ]








from django.urls import path
from . import views

urlpatterns = [
    # path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('<int:student_id>/', views.student_detail, name='student_detail'),
]
