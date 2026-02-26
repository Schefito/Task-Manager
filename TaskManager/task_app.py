from .task_list import TaskList
from .task_stats import TaskStats


class TaskApp:
    def __init__(self, task_list: TaskList):
        self.task_list = task_list
        self.stats = TaskStats()

    def run(self):
        running = True
        while running:
            self.print_menu()
            choice = input("Choose an option: ").strip()
            running = self.handle_choice(choice)

    def print_menu(self):
        print("\n--- TASK MANAGER ---")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Mark as done")
        print("6. Statistics")
        print("7. Exit")

    def handle_choice(self, choice):
        if choice == "1":
            self.add_task()
        elif choice == "2":
            self.show_tasks()
        elif choice == "3":
            self.edit_task()
        elif choice == "4":
            self.delete_task()
        elif choice == "5":
            self.mark_done()
        elif choice == "6":
            self.show_stats()
        elif choice == "7":
            print("Program ended.")
            return False
        else:
            print("Invalid option.")
        return True

    def add_task(self):
        title = input("Title: ").strip()
        if not title:
            print("Title is required.")
            return

        description = input("Description: ").strip()
        try:
            priority = int(input("Priority (1-3): ").strip())
        except ValueError:
            print("Priority must be a number.")
            return

        self.task_list.add_task(title, description, priority)
        print("Task added.")

    def show_tasks(self):
        tasks = self.task_list.get_tasks()
        if not tasks:
            print("No tasks.")
            return

        for task in tasks:
            print(task.format_for_console())

    def edit_task(self):
        self.show_tasks()
        try:
            task_id = int(input("Enter task ID to edit: ").strip())
        except ValueError:
            print("Invalid ID.")
            return

        title = input("New title: ").strip()
        description = input("New description: ").strip()
        priority_raw = input("New priority: ").strip()
        status = input("New status (todo or done): ").strip()

        data = {}
        if title:
            data["title"] = title
        if description:
            data["description"] = description
        if priority_raw:
            try:
                data["priority"] = int(priority_raw)
            except ValueError:
                print("Priority must be a number.")
                return
        if status:
            data["status"] = status

        if self.task_list.edit_task(task_id, data):
            print("Task updated.")
        else:
            print("Task not found.")

    def delete_task(self):
        try:
            task_id = int(input("Enter task ID to delete: ").strip())
        except ValueError:
            print("Invalid ID.")
            return

        self.task_list.delete_task(task_id)
        print("Task deleted.")

    def mark_done(self):
        try:
            task_id = int(input("Enter task ID: ").strip())
        except ValueError:
            print("Invalid ID.")
            return

        if self.task_list.mark_done(task_id):
            print("Task marked as done.")
        else:
            print("Task not found.")

    def show_stats(self):
        tasks = self.task_list.get_tasks()
        print("Total tasks:", self.stats.count_all(tasks))
        print("Completed tasks:", self.stats.count_done(tasks))
