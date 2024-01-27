from Function import get_todos , write_todos
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is ",now)

while True:
    user_action = input("type add ,show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
            todo = user_action[4:]

            todos = get_todos("todos.txt")

            todos.append(todo + '\n')


            with open('todos.txt','w') as file:
                file.writelines(todos)


    elif user_action.startswith("show"):

            todos = get_todos("todos.txt")

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos("todos.txt")


            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos("todos.txt",todos)
        except ValueError:
            print("the command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
                number = int(user_action[9:])

                with open("todos.txt", 'r') as file:
                    todos = file.readlines()

                    index = number - 1
                    todo_to_remove = todos[index].strip("\n")
                    todos.pop(index)

                write_todos("todos.txt",todos)

                message = f"Todo { todo_to_remove} was removed from the list."
                print(message)
        except IndexError:
            print("no item with that number")
            continue
    elif user_action.startswith("exit"):
            break
    else:
        print("the command is not valid")
print("bye")




