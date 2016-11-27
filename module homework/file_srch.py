import os

from sys import argv

x=1
def path_finder():
    try: name = (argv[1])
    except:
        try: name = (input("Ведите путь и название файла"))
        except FileNotFoundError:
             name = (input("Ведите путь и название файла"))

    for root, dirs, files in os.walk("."):
        if name in files:
            print(os.path.join(root, name), os.getcwd())
            symb = (os.getcwd())
        if name in dirs:
            print(os.path.join(root, name), os.getcwd())


if __name__ == "__main__":
    path_finder()
__all__ = ['path_finder', 'x']