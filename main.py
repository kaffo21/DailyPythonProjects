todos = []

while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ").strip().lower()

    match user_action:
        case "add":
            todo = input("Enter todo: ").strip().lower()
            todos.append(todo.capitalize())

        case "show" | "display":
            for index, todo in enumerate(todos):
                print(f"{index+1}. {todo}")

        case "edit":
            number = int(input("Enter the number of todo to edit: ").strip())
            number -= 1 # So we match the Python index system
            existing_todo = todos[number]
            print(f"You are about to edit todo '{existing_todo}':")
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case "complete":
            number = int(input("Enter the number of todo to complete: ").strip())
            todo_remove = todos[number-1]
            todos.pop(number-1)
            print(f"Todo '{todo_remove}' was removed from todo list.")

        case "exit":
            break # Ends the White loop... but the program continues

        case _: # In case there is no match, show the message.
            print("Hey, you entered an unknow command.")

