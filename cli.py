from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, complete or exit: ")
    user_action = user_action.strip()

    #######
    # Add #
    #######
    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = get_todos("todos.txt")

        todos.append(todo + '\n')

        write_todos("todos.txt", todos)

    ########
    # Show #
    ########
    elif user_action.startswith("show"):

        todos = get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    ########
    # Edit #
    ########
    elif user_action.startswith("edit"):

        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos("todos.txt", todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    ############
    # Complete #
    ############
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos("todos.txt", todos)

            print(f"{todo_to_remove} was removed from the list.")

        except IndexError:
            print("There is no item with that number .")
            continue

    ########
    # Exit #
    ########
    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Bye!")
