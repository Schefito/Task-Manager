import unittest
from TaskManager.task import Task


class TestTask(unittest.TestCase):

    def test_init_sets_attributes(self):
        task = Task("Workout", "Gym", 2)

        self.assertEqual(task.title, "Workout")
        self.assertEqual(task.description, "Gym")
        self.assertEqual(task.priority, 2)
        self.assertEqual(task.status, "todo") 

    def test_mark_done_changes_status(self):
        task = Task("Workout", "Gym", 2)
        task.mark_done()

        self.assertEqual(task.status, "done")

    def test_as_dict_returns_expected_keys(self):
        task = Task("Workout", "Gym", 2, status="done")
        data = task.as_dict()

        self.assertEqual(data["title"], "Workout")
        self.assertEqual(data["description"], "Gym")
        self.assertEqual(data["priority"], 2)
        self.assertEqual(data["status"], "done")

    def test_format_for_console_contains_title(self):
        task = Task("Workout", "Gym", 2)
        text = task.format_for_console()

        self.assertIn("Workout", text)


if __name__ == "__main__":
    unittest.main()
