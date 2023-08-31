from StudentApp.views import student_list, course_list
from django.urls import path
from django.contrib import admin
from StudentApp import views
from StudentApp.views import student_list, course_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-list/', student_list),
    path('course-list/', course_list),
]
