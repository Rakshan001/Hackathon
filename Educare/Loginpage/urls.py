from django.contrib import admin
from django.urls import path
from . import views 

# Django admin header customization
admin.site.site_header = "Educare Dashboard"
admin.site.site_title = "Welcome to Educare Dashboard"
admin.site.index_title = "Educare"

urlpatterns = [
    path('signup/', views.SignupPage, name='signup'),
    path('', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('faculty_login/', views.faculty_login, name='faculty_login'),  # Example URL pattern
]
