from django.test import TestCase
from .models import Task

class TaskTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(title="Test task", completed=True)
        self.assertEqual(task.title, "Test task")
        self.assertTrue(task.completed)