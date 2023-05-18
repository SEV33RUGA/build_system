import yaml
import os
from docopt import docopt


usage = """

Usage:
    main.py list (builds | tasks)
    main.py get build <build_name>
    main.py get task <task_name>


Options:
    -h --help   Show this screen.
    
"""


def get_yaml(file: str):
    if not isinstance(file, str):
        raise TypeError("File only string type")

    file = os.path.normpath(file)

    if os.path.isdir(file):
        raise NotADirectoryError("Only file, not a directory")

    if not os.path.exists(file):
        raise FileNotFoundError(f"No such file: '{file}'")

    try:
        with open(file, "r") as f:
            return yaml.safe_load(f)
    except Exception:
        raise TypeError(f"File {file} not correct")


def decorator_show(func):

    def inner(*args, **kwargs):
        d = [*args][0]

        if len([*args]) == 2:
            if not isinstance([*args][1], str):
                raise TypeError("Name only string type")

        if not isinstance(d, dict):
            raise TypeError("Only dictionary")

        if len(d) == 0:
            raise KeyError("Dictionary is empty")

        try:
            result = func(*args, **kwargs)
            return result
        except Exception as error:
            raise KeyError(f"Dictionary not correct: {error}")

    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner


@decorator_show
def show_names(d: dict):
    dict_name = str(*d)
    names = []

    for item in d[dict_name]:
        if len(names) == 0:
            print(f"List of available {dict_name}:")
        name = item['name']
        names.append(name)
        print(f" * {name}")
    return names


@decorator_show
def show_name_details(d: dict, name: str):
    dict_name = str(*d)
    for a in d[dict_name]:
        if a["name"] == name:

            print(f"{dict_name[:-1].capitalize()} info:")
            print(f" * name: {name}")

            items_name = [*a][1]
            print(f" * {items_name}:", end="")
            if len(a[items_name]) > 0:
                for item in a[items_name]:
                    print(f" {item},", end="")
                print("", end="\b \n")
            else:
                print()

            return True

    print(f"Not found {dict_name[:-1]} name: {name}")
    return False


def main():
    builds = get_yaml("builds.yaml")
    tasks = get_yaml("tasks.yaml")
    args = docopt(usage)

    if args["list"]:
        if args["builds"]:
            show_names(builds)
        elif args["tasks"]:
            show_names(tasks)

    if args["get"]:
        if args["build"]:
            show_name_details(builds, args["<build_name>"])
        elif args["task"]:
            show_name_details(tasks, args["<task_name>"])


if __name__ == '__main__':
    main()
