def write_todos(filepath, todos_arg):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)
