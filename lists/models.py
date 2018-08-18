from django.db import models

class TodoList(models.Model):
    title = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.created}: {len(self.todo_items.all())} items'

    class Meta:
        ordering = ['-created']

class TodoItem(models.Model):
    task = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='todo_items')

    def __str__(self):
        return f'{self.todo_list.title}: {self.task}'
