from django.test import TestCase
from tasks.models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(name="run a test")

    def test_task_models(self):
        task = Task.objects.get(name="run a test")
        self.assertEqual(task.name, "run a test")
