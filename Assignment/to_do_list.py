def to_do_list():
    print("=" * 29)
    print("SEMICOLON TO-DO LIST MANAGER")
    print("=" * 29)
    print(""" 1. Add a task 
 2. View tasks 
 3. Mark task as complete 
 4. Delete a task 
 5. Exit """)
    
    tasks = []
    while True:
        option = input("Enter your choice: ")
        while option not in ["1", "2", "3", "4", "5"]:
            print("Choose the right options (1 - 5)")
            print("")
            option = input("Enter your choice: ")

        match option:
            case "1":
                task_name = input("Add a task: ")
                while task_name == "":
                    print("You have to add a task")
                    task_name = input("Add a task: ")
                tasks.append({"name": task_name, "status": "[]"})
                print(f"{task_name}>>>>>>>>>>>>>>>")
                print("Task added successfully!")
            
            case "2":
                if tasks == []:
                    print("No task added yet")
                else:
                    print("Tasks")
                    for index, task in enumerate(tasks):
                        print(f"{index+1}. {task['name']} {task['status']}")
            
            case "3":
                if tasks == []:
                    print("No task added yet")
                else:
                    print("Tasks")
                    for index, task in enumerate(tasks):
                        print(f"{index+1}. {task['name']} {task['status']}")
                    task_index = int(input("Enter the task number to mark as complete: ")) - 1
                    if task_index < len(tasks):
                        tasks[task_index]["status"] = "[X]"
                        print(f"{index+1}. {task['name']} {task['status']}")
                        print("Task marked as complete!")
                    else:
                        print("Invalid task number!")
            
            case "4":
                if tasks == []:
                    print("No task added yet")
                else:
                    print("Tasks")
                    for index, task in enumerate(tasks):
                        print(f"{index+1}. {task['name']} {task['status']}")
                    task_index = int(input("Enter the task number to delete: ")) - 1
                    if task_index < len(tasks):
                        del tasks[task_index]
                        print("Task deleted successfully!")
                    else:
                        print("Invalid task number!")
            
            case "5":
                print("Exit")
                break

to_do_list()

