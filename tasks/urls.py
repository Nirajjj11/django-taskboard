from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="task"),
    path("add-task/", views.add_task, name="add_task"),
]
