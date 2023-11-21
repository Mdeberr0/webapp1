FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Returns the intems in a file as a list """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos( todos_arg, filepath=FILEPATH):
    """ Writes items from a list to a file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello from functions")
    # prints only when you run this file directly. Won't print using import in another file
    # debug uses