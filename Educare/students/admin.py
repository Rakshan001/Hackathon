from django.contrib import admin
from .models import Student, School, SchoolHistory, Achievement

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'unique_id', 'roll_no', 'student_class', 'current_school')
    search_fields = ('name', 'unique_id', 'roll_no')
    list_filter = ('student_class', 'current_school')
    readonly_fields = ('unique_id',)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number')
    search_fields = ('name',)

class SchoolHistoryAdmin(admin.ModelAdmin):
    list_display = ('student', 'school', 'start_date', 'end_date')
    search_fields = ('student__name', 'school__name')
    list_filter = ('school', 'start_date', 'end_date')

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('student', 'event', 'type', 'level', 'date')
    search_fields = ('student__name', 'event', 'type', 'level')
    list_filter = ('type', 'level', 'date')

admin.site.register(Student, StudentAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(SchoolHistory, SchoolHistoryAdmin)
admin.site.register(Achievement, AchievementAdmin)
