# Python package for creating beautiful command line interfaces in a composable way with as little code as necessary.
import click 

@click.group
def mycommands():
    pass

@click.command()
@click.option("--name", prompt="Enter you name: ", help="The name of the user")
def hello(name):
    click.echo(f"Hello {name}!")

PRIORITIES = {
    "o": "Optional",
    "l": "Low",
    "m": "Medium,",
    "h": "High",
    "c": "Crucial"
}

@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys(), default = "m"))
@click.argument("todofile", type=click.Path(exists=False), required=0)
@click.option("-n", "--nname", prompt="Enter the todo name", help="The name of the todo item")
@click.option("-d", "--desc", prompt="Describe the todo", help="The description of the todo item")
def add_todo(name, description, priority, toDoFile):
    filename = toDoFile if toDoFile is not None else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"{name}: {description} [Priority: {PRIORITIES[priority]}]\n")

@click.command()
@click.argument("idx", type=int, required=1)
def delete_todo(idx):
    with open("mytodos.txt", "r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open("mytodos.txt", "w") as f:
        f.write("\n".join(todo_list))
        f.write("\n")

@click.command()
@click.option("-p", "--priorty", type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile", type=click.Path(exists=True), required=0)
def list_todo(priority, toDofile):
    filename = toDofile if toDofile is not None else "mytodos.txt"
    with open (filename, "r") as f:
        toDoList = f.read().splitlines()
    if priority is None:
        for idx, toDo in enumerate(toDoList):
            print(f"({idx}) - {toDo}")
    else:
        for idx, toDo in enumerate(toDoList):
            if f"[Priority: {PRIORITIES[priority]}]" in toDo:
                print(f"({idx}) - {toDo}")

mycommands.add(hello)
mycommands.add(add_todo)
mycommands.add(delete_todo)
mycommands.add(list_todo)

if __name__ == "__main__":
    mycommands()