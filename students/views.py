from django.shortcuts import render
from .models import Student


def student_schema(request):
	fields = Student._meta.fields
	return render(request, "students/student_schema.html", {"fields": fields})
