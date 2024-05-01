from django.urls import path
from .views import register, login_view, logout_view, task_list, add_task, delete_task

app_name = "todo"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("tasks/", task_list, name="task_list"),
    path("tasks/add/", add_task, name="add_task"),
    path("tasks/delete/<int:task_id>/", delete_task, name="delete_task"),
]
