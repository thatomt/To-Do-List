def show_tasks(tasks):
    """
    A function to display the current list of tasks in a to-do list application. 
    It takes a list of tasks as input and prints them in a numbered format. 
    If there are no tasks, it informs the user that there are no tasks yet.

    """

    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = inpit("Enter a new task: ")
    task.append(task)
    print("Task added")
