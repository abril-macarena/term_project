#MAIN FLOW SPACE
"""
START

DISPLAY main menu (which contains the following): 
1. add a new task
2. view tasks 
3. edit a task
4. send reminder
4. exit

WHILE user doesn't select "Exit":
    IF user selects "Add a new task":
        CALL add_task()
    ELSE IF user selects "View tasks":
        CALL view_tasks()
    ELSE IF user selects "Edit a task":
        CALL edit_task()
    ELSE IF user selects "Send reminders":
        CALL send_reminders()

END
"""

#ADDING A NEW TASK
"""
FUNCTION add_task():
  PROMPT user for task title
  PROMPT user for task due date (in format YYYY-MM-DD)
  PROMPT user for task importance (1 to 5)
  PROMPT user for task type (e.g., "work", "personal", "exercise")

  CONVERT due date string to a date object
  CREATE a new task object with the title, due date, and type
  ADD the new task to the task list
  DISPLAY "Task added successfully!"

  RETURN
"""

#VIEWING TASKS
"""
FUNCTION view_tasks():
    IF task list is empty:
        DISPLAY "No tasks available."
        RETURN

    DISPLAY all tasks (include index (e.g., 1, 2, 3) for easier selection later)
    FOR each task in the task list:
        DISPLAY task index, title, due date, importance, and type

    SORT tasks by due date in ascending order
    DISPLAY sorted task list

    RETURN
"""

#EDITING A TASK
"""
FUNCTION edit_task():
    CALL view_tasks()

    IF task list is empty:
        DISPLAY "No tasks available to edit."
        RETURN

    PROMPT user to select a task by index
    VALIDATE the selected index

    DISPLAY the selected task's details
    PROMPT user to choose a field to edit (title, due date, importance, type)
    PROMPT user for the new value

    UPDATE the selected field in the task
    DISPLAY "Task updated successfully!"

    RETURN
"""

#SENDING CONTEXT AWARE REMINDERS
"""
FUNCTION send_reminders():
    FOR each task in the task list:
        CALCULATE days_until_due as (task.due_date - current_date)

    IF days_until_due <= 1:
        CALL check_reminder_time(task.type)
        IF reminder time is appropriate:
            DISPLAY "Reminder: [task title] is due soon!"

    RETURN
"""

#CHECKING REMINDER TIME
"""
FUNCTION check_reminder_time(task_type):
    GET current hour
    DEFINE time rules:
        - "work" reminders: 9 AM to 5 PM
        - "personal" reminders: 6 PM to 10 PM
        - "exercise" reminders: 6-8 AM or 6-8 PM

    RETURN True if the current time matches the rule for task_type, otherwise False

"""

#DATA STRUCTURE FOR TASKS
"""
DEFINE a Task object with:
    - title (string)
    - due_date (date object)
    - importance (integer 1-5)
    - type (string, e.g., "work", "personal", "exercise")

STORE all tasks in a task_list (a list of Task objects)
"""

#EXIT PROGRAM
"""
IF user selects "Exit":
    DISPLAY "Goodbye!"
    STOP program
"""