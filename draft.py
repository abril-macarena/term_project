import datetime 

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
task_list = []

def display_menu():
    print("Automated Task Management Assistant")
    print("1. Add a new task")
    print("2. View tasks")
    print("3. Edit a task")
    print("4. Send reminders")
    print("5. Exit")
#this is separate from the main function which will execute the while/if/else loops mentioned in the pseudocode


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
def add_task():
    title = input("Enter task title: ")
    due_date_str = input("Enter task due date (YYYY-MM-DD): ")
    importance = int(input("Enter task importance (1-5): "))
    task_type = input("Enter task type (e.g., 'work', 'personal', 'exercise'): ")

    #convert due date from string to date
    try:
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Task not added.")
        return
    
    task = {
        "title": title,
        "due_date": due_date,
        "importance": importance,
        "type": task_type
    }
    
    task_list.append(task)
    print("Task added successfully!")
    

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
def view_tasks():
    if len(task_list) == 0:
        print("No tasks available.")
        return

    #sort tasks by due date
    sorted_tasks = []
    for task in task_list:
        sorted_tasks.append(task)
    sorted_tasks.sort(key=lambda t: t["due_date"])
    
    #display tasks
    task_number = 1
    for task in sorted_tasks:
        print("\nTask", task_number, ":")
        print("  Title:", task["title"])
        print("  Due Date:", task["due_date"])
        print("  Importance:", task["importance"])
        print("  Type:", task["type"])
        task_number += 1

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
def edit_task():
    view_tasks()
    if not task_list:
        return
    
    try:
        task_index = int(input("\nEnter the task number to edit: ")) - 1
        if task_index < 0 or task_index >= len(task_list):
            print("Invalid task number.")
            return
    except ValueError:
        print("Invalid input.")
        return
    
    task = task_list[task_index]
    print(f"\nEditing Task: {task['title']}")
    print("1. Edit Title")
    print("2. Edit Due Date")
    print("3. Edit Importance")
    print("4. Edit Type")
    
    try:
        choice = int(input("Select a field to edit (e.g. 1-5): "))
    except ValueError:
        print("Invalid choice.")
        return
    
    if choice == 1:
        task["title"] = input("Enter new title: ")
    elif choice == 2:
        new_date = input("Enter new due date (YYYY-MM-DD): ")
        try:
            task["due_date"] = datetime.datetime.strptime(new_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format.")
    elif choice == 3:
        try:
            task["importance"] = int(input("Enter new importance (1-5): "))
        except ValueError:
            print("Invalid input.")
    elif choice == 4:
        task["type"] = input("Enter new type: ")
    else:
        print("Invalid choice.")
    
    print("Task updated successfully!")



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
def send_reminders():
    current_date = datetime.date.today()
    current_hour = datetime.datetime.now().hour
    
    for task in task_list:
        days_until_due = (task["due_date"] - current_date).days
        if days_until_due <= 1:
            if check_reminder_time(task["type"], current_hour):
                print(f"Reminder: '{task['title']}' is due soon!")


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
def check_reminder_time(task_type, current_hour):
    if task_type == "work":
        return 9 <= current_hour <= 17
    elif task_type == "personal":
        return 18 <= current_hour <= 22
    elif task_type == "exercise":
        return (6 <= current_hour <= 8) or (18 <= current_hour <= 20)
    return True

#DATA STRUCTURE FOR TASKS - this was accomplished in the first function as opposed to being its own 
"""
DEFINE a Task object with:
    - title (string)
    - due_date (date object)
    - importance (integer 1-5)
    - type (string, e.g., "work", "personal", "exercise")

STORE all tasks in a task_list (a list of Task objects)
"""

#EXIT PROGRAM - accomplished during main function - does not need to be a seperate function
"""
IF user selects "Exit":
    DISPLAY "Goodbye!"
    STOP program
"""

###MAIN FUNCTION THAT EXECUTES PROGRAM
def main():
    while True:
        display_menu()
        try:
            choice = int(input("Select an option (e.g. 1-5): "))
        except ValueError:
            print("Invalid input.")
            continue
        
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            edit_task()
        elif choice == 4:
            send_reminders()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")