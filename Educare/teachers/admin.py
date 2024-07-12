from django.contrib import admin
from .models import Batch, Subject, SubjectGroup, Enrollment, Marks

class BatchAdmin(admin.ModelAdmin):
    list_display = ('school', 'start_year', 'end_year')
    list_filter = ('school', 'start_year', 'end_year')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SubjectGroupAdmin(admin.ModelAdmin):
    list_display = ('batch',)
    filter_horizontal = ('subjects',)

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'batch', 'subject_group')
    list_filter = ('batch', 'subject_group', 'student')

class MarksAdmin(admin.ModelAdmin):
    list_display = ('get_student_name', 'get_student_roll_no', 'get_batch', 'subject', 'ia1_marks', 'ia2_marks', 'ia3_marks', 'midterm_marks', 'final_marks', 'total')
    list_filter = ('enrollment__batch', 'subject', 'enrollment__student')

    def get_student_name(self, obj):
        return obj.enrollment.student.name
    get_student_name.short_description = 'Student Name'

    def get_student_roll_no(self, obj):
        return obj.enrollment.student.roll_no
    get_student_roll_no.short_description = 'Roll No'

    def get_batch(self, obj):
        return obj.enrollment.batch
    get_batch.short_description = 'Batch'

admin.site.register(Batch, BatchAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectGroup, SubjectGroupAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Marks, MarksAdmin)
