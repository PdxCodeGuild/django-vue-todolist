from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from lists.models import TodoList, TodoItem
from lists.serializers import TodoListSerializer, TodoItemSerializer

@api_view(['GET'])
def todo_lists(request):
  todo_lists = TodoList.objects.all()
  serialized_todo_lists = TodoListSerializer(todo_lists, many=True)
  return Response(serialized_todo_lists.data)

@api_view(['POST'])
def create_todo_list(request):
  todo_list = TodoList.objects.create(title=request.data['title'])
  todo_list.save()
  serialized_todo_list = TodoListSerializer(todo_list)

  return Response(serialized_todo_list.data)

@api_view(['POST'])
def create_todo_item(request):
  todo_list = TodoList.objects.get(id=request.data['list_id'])
  todo_item = TodoItem.objects.create(
    task=request.data['task'],
    todo_list=todo_list,
  )
  todo_item.save()
  serialized_todo_item = TodoItemSerializer(todo_item)
  return Response(serialized_todo_item.data)

@api_view(['POST'])
def toggle_todo_item(request):
  todo_item = TodoItem.objects.get(id=request.data['item_id'])
  todo_item.completed = not todo_item.completed
  todo_item.save()

  return Response({'completed': todo_item.completed})

@api_view(['POST'])
def delete_todo_item(request):
  todo_item = TodoItem.objects.get(id=request.data['item_id'])
  todo_item.delete()

  return Response({'deleted': True})