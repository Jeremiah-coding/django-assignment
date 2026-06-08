from django.db import models
from departments.models import Department


class Student(models.Model):
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	email = models.EmailField(unique=True)
	student_id = models.CharField(max_length=25, unique=True)
	department = models.ForeignKey(
		Department,
		on_delete=models.CASCADE,
		related_name="students"
	)
	year_level = models.PositiveIntegerField()
	enrolled_at = models.DateField()

	def __str__(self):
		return f"{self.student_id} - {self.first_name} {self.last_name}"
