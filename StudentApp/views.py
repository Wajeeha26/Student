import json
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Course
from django.http import JsonResponse


@api_view(['GET','POST','PUT'])
def student_list(request):
    students = Student.objects.all()
    student_list = []

    for student in students:
        student_data = {
            'student name': student.student_name,
            'contact_no': student.contact_no,
            'address': student.address,
            'date_of_birth': student.date_of_birth,
            'reg_no': student.reg_no,
            'course': student.course.course,
            'semester': student.semester,
            'Degree': student.Degree,
        }
        student_list.append(student_data)
    
    if request.method == 'GET':
        return Response(student_list)
    elif request.method == 'PUT':
        # Handle PUT logic here
        return Response({'message': 'PUT method'})
    elif request.method == 'POST':
        data = request.data
        print(data)
        return Response({'message': 'POST method'})
   
    return Response(student_list)

@api_view(['GET','POST','PUT'])
def course_list(request):
    courses = Course.objects.all()
    course_list = []

    for course in courses:
        course_data = {
            'course_id': course.id,
            'course_name': course.course,
        }
        course_list.append(course_data)

    return Response(course_list)

