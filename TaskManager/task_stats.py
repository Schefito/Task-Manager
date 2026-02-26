from .task import Task


class TaskStats:
    def count_all(self, tasks: list[Task]):
        return len(tasks)

    def count_done(self, tasks: list[Task]):
        return sum(1 for t in tasks if t.status == "done")
