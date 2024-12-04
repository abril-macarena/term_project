from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

task_list = []

#HOME PAGE
@app.route("/")
def home():
    return render_template("home.html")

#VIEW TASKS
@app.route("/tasks")
def view_tasks():
    #sorts tasks by due date
    sorted_tasks = sorted(task_list, key=lambda t: t["due_date"])
    return render_template("tasks.html", tasks=sorted_tasks)

#ADD TASK
@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form.get("title")
        due_date_str = request.form.get("due_date")
        importance = int(request.form.get("importance"))
        task_type = request.form.get("type")

        try:
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except ValueError:
            return render_template("add_task.html", error="Invalid date format.")

        task = {
            "title": title,
            "due_date": due_date,
            "importance": importance,
            "type": task_type
        }
        task_list.append(task)
        return redirect(url_for("view_tasks"))

    return render_template("add_task.html")

#EDIT TASK
@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if task_id < 0 or task_id >= len(task_list):
        return "Task not found."

    task = task_list[task_id]
    if request.method == "POST":
        task["title"] = request.form.get("title")
        task["due_date"] = datetime.datetime.strptime(request.form.get("due_date"), "%Y-%m-%d").date()
        task["importance"] = int(request.form.get("importance"))
        task["type"] = request.form.get("type")
        return redirect(url_for("view_tasks"))

    return render_template("edit_task.html", task=task, task_id=task_id)

#SENDING REMINDERS
@app.route("/reminders")
def send_reminders():
    current_date = datetime.date.today()
    current_hour = datetime.datetime.now().hour
    reminders = []

    for task in task_list:
        days_until_due = (task["due_date"] - current_date).days
        if days_until_due <= 1:
            if check_reminder_time(task["type"], current_hour):
                reminders.append(f"Reminder: '{task['title']}' is due soon!")

    return render_template("reminders.html", reminders=reminders)

#HELPER FUNCTION - checking reminder time
def check_reminder_time(task_type, current_hour):
    if task_type == "Work":
        return 9 <= current_hour <= 17
    elif task_type == "Personal":
        return 18 <= current_hour <= 22
    elif task_type == "Exercise":
        return (6 <= current_hour <= 8) or (18 <= current_hour <= 20)
    return True

#RUNING APP
if __name__ == "__main__":
    app.run(debug=True)
