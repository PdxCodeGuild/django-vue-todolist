from django.urls import path

from lists import views

app_name = 'lists'
urlpatterns = [
    path('', views.todo_lists, name='todo_lists'),
    path('create', views.create_todo_list, name='create_todo_list'),
    path('items/create', views.create_todo_item, name='create_todo_item'),
    path('items/toggle', views.toggle_todo_item, name='toggle_todo_item'),
    path('items/delete', views.delete_todo_item, name='delete_todo_item'),            
]