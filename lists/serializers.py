from rest_framework import serializers

from lists.models import TodoList, TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'task', 'completed', 'completed_at')

class TodoListSerializer(serializers.ModelSerializer):
    todo_items = TodoItemSerializer(many=True)

    class Meta:
        model = TodoList
        fields = ('id', 'title', 'created', 'todo_items')
