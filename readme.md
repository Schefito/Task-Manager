# Task Manager – Python & SQLite Application

A professional console-based task management system designed with **Object-Oriented Programming (OOP)** principles and persistent data storage.

##  Overview
**Task Manager** is a Python application that allows users to manage their daily workflows efficiently. All data is stored in a **SQLite database**, ensuring that your tasks are saved even after closing the application.

### Key Features:
* **Full CRUD Operations:** Add, display, edit, and delete tasks with ease.
* **Data Persistence:** Real-time synchronization with an SQLite database (`tasks` file).
* **Priority System:** Organize tasks using a 1–3 scale.
* **Status Tracking:** Easily mark tasks as "done" or "todo".

---

## Class Design & Architecture
The project follows a modular design to ensure high maintainability and clear responsibility for each component:

### 1. `Task` (Data Model)
Represents a single task entity.
* **Fields:** `id`, `title`, `description`, `priority`, and `status`.
* **Methods:** `mark_done()` (completes task) and `update()` (modifies data).

### 2. `TaskDbManager` (Data Access Layer)
Handles all communication with the **SQLite database** using SQL queries.
* **Methods:** `add_task`, `get_tasks`, `update_task`, `delete_task`.

### 3. `TaskList` (Business Logic)
Contains the core logic for managing the task collection and coordinating between the UI and Database.

### 4. `TaskStats` (Analytics)
A utility class that provides simple statistics, such as total task count and completion rates.

### 5. `TaskApp` (Presentation Layer)
The console-based user interface that handles user input and menu navigation.

---

## Tech Stack
* **Language:** Python 3.x
* **Database:** SQLite
* **Concepts:** Object-Oriented Programming (OOP), Data Persistence, Clean Code
