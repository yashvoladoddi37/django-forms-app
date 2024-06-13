from django.urls import path
from .views import index, delete_task, toggle_task

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', toggle_task, name='toggle_task'),
]
