from django.urls import path
from .views import todo_list
# App Name.
app_name = 'todo'

# Create your urls here.
urlpatterns = [
    path('list/', todo_list, name='todo_list'),
]