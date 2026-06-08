from django.shortcuts import render
from .models import Department


def department_list(request):
	departments = Department.objects.all().order_by("code")
	return render(
		request,
		"departments/department_list.html",
		{"departments": departments},
	)
