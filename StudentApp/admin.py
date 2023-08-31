from django.contrib import admin
from django.contrib import admin
from StudentApp.models import Student
from StudentApp.models import Course
class StudentAdmin(admin.ModelAdmin):
    list_display=('student_name', 'contact_no', 'address', 'date_of_birth', 'reg_no', 'course', 'semester', 'Degree','Student_image_NEW')
class CourseAdmin(admin.ModelAdmin):
    list_display=('course',)

admin.site.register(Course,CourseAdmin)
admin.site.register(Student,StudentAdmin)
