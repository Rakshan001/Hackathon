from django.contrib import admin
from .models import Batch, Subject, Enrollment, Marks
from students.models import Student

class BatchAdmin(admin.ModelAdmin):
    list_display = ('start_year', 'end_year')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'batch', 'subject')
    list_filter = ('batch', 'subject', 'student')

class MarksAdmin(admin.ModelAdmin):
    list_display = ('get_student_name', 'get_student_roll_no','get_batch', 'get_subject', 'ia1_marks', 'ia2_marks', 'ia3_marks', 'midterm_marks', 'final_marks', 'total')
    list_filter = ('enrollment__batch', 'enrollment__subject', 'enrollment__student',)



    def get_student_name(self, obj):
        return obj.enrollment.student.name
    get_student_name.short_description = 'Student Name'

    def get_student_roll_no(self, obj):
        return obj.enrollment.student.roll_no
    get_student_roll_no.short_description = 'Roll No'

    def get_student_class(self, obj):
        return obj.enrollment.student.class_name
    get_student_class.short_description = 'Class'

    def get_batch(self, obj):
        return obj.enrollment.batch
    get_batch.short_description = 'Batch'

    def get_subject(self, obj):
        return obj.enrollment.subject
    get_subject.short_description = 'Subject'

admin.site.register(Batch, BatchAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Marks, MarksAdmin)







from django.contrib import admin
from .models import Achievement

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('student', 'event', 'type', 'level', 'date', 'outcome')
    list_filter = ('student', 'type', 'level')

admin.site.register(Achievement, AchievementAdmin)


