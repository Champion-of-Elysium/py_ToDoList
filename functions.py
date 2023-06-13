def get_todos(filepath):
    with open(filepath, "r") as file:
        todos = file.readlines()
        return todos


def write_todos(filepath, todos_args):
    with open(filepath, "w") as file:
        file.writelines(todos_args)
