from .task_db_manager import TaskDbManager
from .task import Task


class TaskList:
    def __init__(self, db_manager: TaskDbManager):
        self.db = db_manager

    def add_task(self, title, description, priority):
        task = Task(title, description, priority)
        self.db.add_task(task)
        return task

    def get_tasks(self):
        return self.db.get_tasks()

    def edit_task(self, task_id, data: dict):
        tasks = self.db.get_tasks()
        for task in tasks:
            if task.id == task_id:
                task.title = data.get("title", task.title)
                task.description = data.get("description", task.description)
                task.priority = data.get("priority", task.priority)
                task.status = data.get("status", task.status)
                self.db.update_task(task)
                return True
        return False

    def delete_task(self, task_id):
        self.db.delete_task(task_id)

    def mark_done(self, task_id):
        tasks = self.db.get_tasks()
        for task in tasks:
            if task.id == task_id:
                task.mark_done()
                self.db.update_task(task)
                return True
        return False
