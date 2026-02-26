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
    
def remove_task(tasks):
    show_tasks(tasks)
    if tasks:
        index = int(input("Enter task number to remove: "))
        task.pop(index -1)
        print("Task removed.")

tasks = []

while True:
    print(" 1. Add task")
    print(" 2. View Task")
    print(" 3. Remove Task")
    choice = input("Choose an option: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        show_tasks(tasks)
