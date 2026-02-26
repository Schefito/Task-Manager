import unittest
from TaskManager.task_list import TaskList
from TaskManager.task import Task


class FakeTaskDbManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, task):
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)
        return task.id

    def get_tasks(self):
        return list(self.tasks)

    def update_task(self, task):
        for i, t in enumerate(self.tasks):
            if t.id == task.id:
                self.tasks[i] = task

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]


class TestTaskList(unittest.TestCase):

    def setUp(self):
        self.fake_db = FakeTaskDbManager()
        self.task_list = TaskList(self.fake_db)

    def test_add_task_saves_task(self):
        self.task_list.add_task("Workout", "Gym", 2)
        tasks = self.task_list.get_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Workout")

    def test_mark_done_changes_status(self):
        self.task_list.add_task("Workout", "Gym", 2)
        task_id = self.task_list.get_tasks()[0].id

        self.task_list.mark_done(task_id)

        self.assertEqual(self.task_list.get_tasks()[0].status, "done")

    def test_delete_task_removes_task(self):
        self.task_list.add_task("Workout", "Gym", 2)
        task_id = self.task_list.get_tasks()[0].id

        self.task_list.delete_task(task_id)

        self.assertEqual(len(self.task_list.get_tasks()), 0)


if __name__ == "__main__":
    unittest.main()
