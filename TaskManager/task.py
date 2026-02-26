
class Task:
    def __init__(self, title, description, priority, status="todo"):
        self.id = None
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def mark_done(self):
        self.status = "done"

    def as_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
        }
    
    def format_for_console(self):
        if self.id is not None:
            prefix = f"[{self.id}] "
        else:
            prefix = ""
        return f"{prefix}{self.title} | {self.description} | priority: {self.priority} | status: {self.status}"
