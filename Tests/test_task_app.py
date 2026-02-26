import unittest
from TaskManager.task_app import TaskApp

class FakeTaskList:
    pass


class TestTaskApp(unittest.TestCase):

    def test_init_stores_task_list(self):
        fake_list = FakeTaskList()
        app = TaskApp(fake_list)
        self.assertIs(app.task_list, fake_list)


if __name__ == "__main__":
    unittest.main()
