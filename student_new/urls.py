from django.urls import path, include
from django.contrib import admin
from StudentApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('students/', views.student_list, name='student_list'),
    path('courses/', views.course_list, name='course_list'),
     path('', views.student_list, name='default_home'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
