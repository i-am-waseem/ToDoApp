from django.db import models

# Create your models here.
class TodoTask(models.Model):

    def __str__(self):
        return self.todo_task

    todo_task = models.TextField(max_length = 200)
    task_created = models.DateTimeField('task created')
