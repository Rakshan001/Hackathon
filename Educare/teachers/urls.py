from django.urls import path
from . import views

urlpatterns = [
    # path('profile/', views.update_profile, name='profile'),
    path('marks/', views.view_marks, name='view_marks'),
]
