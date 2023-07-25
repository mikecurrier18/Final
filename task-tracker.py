def load_tasks():
    try:
        # Tries to open "tasks.txt" file + get tasks
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
        return tasks
    except FileNotFoundError:
        # If no "tasks.txt" found, returns empty list
        return []

def save_tasks(tasks):
    # Opens "tasks.txt" + saves each task on new line
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        # If no tasks already, prints the following:
        print("No tasks in your to-do list yet. Try creating one and check back here again!")
    else:
        # If there's tasks already, displays each with index value
        print("Tasks in your to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks, new_task):
    # Adds new_task to tasks
    tasks.append(new_task)
    print(f"Task '{new_task}' added to your to-do list!")

def remove_task(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        # If task_number is valid, removes task from list
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed from your to-do list.")
    else:
        # If task_number input is invalid, prints the following:
        print("Invalid task number, please try again.")

def get_valid_choice(prompt, valid_choices):
    while True:
        # Asks for input using prompt
        choice = input(prompt)
        if choice in valid_choices:
            # If input is one of the valid choices, returns choice
            return choice
        print("Invalid choice, please try again. Task numbers can be 1 (view tasks), 2 (add a task), 3 (remove a task), or 4 (exit).")

def main():
    # Loads tasks from "tasks.txt" at the start of the program
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List Manager =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        # Gets a user input (1, 2, 3, or 4) using get_valid_choice function
        choice = get_valid_choice("Enter your choice (1/2/3/4): ", ["1", "2", "3", "4"])

        if choice == "1":
            # If "1", displays the tasks
            display_tasks(tasks)
        elif choice == "2":
            # If "2", asks for a new task and adds it to the list
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
            # Saves the updated tasks list to "tasks.txt"
            save_tasks(tasks)
        elif choice == "3":
            # If "3", displays tasks and asks for the task number to remove
            display_tasks(tasks)
            task_number = int(get_valid_choice("Enter the task number to remove: ", [str(i) for i in range(1, len(tasks) + 1)]))
            # Removes the selected task if the task_number is valid
            remove_task(tasks, task_number)
            # Saves the updated tasks list to "tasks.txt"
            save_tasks(tasks)
        elif choice == "4":
            # If "4", exits the program and prints the following:
            print("Exiting To-Do List Manager. Any updates you have been made are now visible in your tasks.txt file. Have a great day!")
            break

if __name__ == "__main__":
    # Starts the program by calling the main() function
    main()
