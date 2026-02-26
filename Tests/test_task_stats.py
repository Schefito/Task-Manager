import unittest
from TaskManager.task_stats import TaskStats
from TaskManager.task import Task


class TestTaskStats(unittest.TestCase):

    def setUp(self):
        self.stats = TaskStats()
        self.tasks = [
            Task("Workout", "Gym", 1, status="done"),
            Task("Study", "Software Testing", 2, status="todo"),
            Task("Cleaning", "Kitchen", 3, status="done"),
        ]

    def test_count_all(self):
        self.assertEqual(self.stats.count_all(self.tasks), 3)

    def test_count_done(self):
        self.assertEqual(self.stats.count_done(self.tasks), 2)


if __name__ == "__main__":
    unittest.main()
