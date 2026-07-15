def main():
    tasks = []

    while True:
        # Display the menu
        print("\n--- To-Do List Menu ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        # 1. Add tasks
        if choice == '1':
            task = input("Enter the task description: ")
            tasks.append(task)
            print(f"✅ Task '{task}' added successfully!")
            
        # 2. View tasks
        elif choice == '2':
            print("\n--- Your Tasks ---")
            if not tasks:
                print("Your list is currently empty.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                    
        # 3. Delete tasks
        elif choice == '3':
            if not tasks:
                print("No tasks to delete. Your list is empty.")
                continue
                
            # Show tasks so the user knows which number to pick
            print("\n--- Your Tasks ---")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
                
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"🗑️ Task '{removed_task}' deleted successfully!")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")
                
        # Exit the program
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
            
        # Handle invalid inputs
        else:
            print("❌ Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()