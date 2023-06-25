from django.shortcuts import render
from .models import Course

from django.http import HttpResponse
# Create your views here.

def course(self):
    course_2 = Course(name = "SQL", comission = 25635)
    course_2.save()
    document = f"Curso: {course_2.name} - Comission: {course_2.comission}"
    return HttpResponse(document)