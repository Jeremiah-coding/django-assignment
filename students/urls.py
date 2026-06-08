from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("schema/", views.student_schema, name="schema"),
]
