Task Manager – task management application

1. Overview
Task Manager is a console application written in Python that allows managing a task list. Task data are stored in a SQLite database.

Users can:
- add new tasks,
- display the task list,
- edit existing tasks,
- delete tasks,
- change task status.

2. Main features
1. Adding a task:
   - title,
   - description,
   - priority (1–3),
   - default status “todo”.

2. Displaying the task list:
   - a readable list in the console.

3. Editing a task:
   - change title, description, priority, or status.

4. Deleting a task:
   - remove a task by ID.

5. Changing task status:
   - mark a task as “done”.

3. Class design and responsibilities

1. Class Task
Represents a single task.

Fields:
- id,
- title,
- description,
- priority,
- status.

Methods:
- mark_done() – marks the task as completed,
- update(...) – updates task data.

2. Class TaskDbManager
Handles communication with the SQLite database.

Methods:
- add_task(task),
- get_tasks(),
- update_task(task),
- delete_task(task_id).

3. Class TaskList
Contains logic for managing the task list.

Methods:
- add_task(data),
- edit_task(task_id, data),
- delete_task(task_id),
- mark_done(task_id),
- get_tasks().

4. Class TaskStats
Provides simple statistics.

Methods:
- count_all(),
- count_done().

5. Class TaskApp
Console interface for the application.

Methods:
- run(),
- print_menu(),
- handle_choice().
