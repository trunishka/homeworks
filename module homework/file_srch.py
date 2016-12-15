import os

from sys import argv


def filename():
    if len(argv) > 1:
        file_name = argv[1]
    else:
        file_name = input("insert the name")
    while file_name not in os.listdir():
            file_name = input("insert the name")
    return file_name


def path_finder(x):
        for root, dirs, files in os.walk("."):
            if x in files:
                return((os.path.join(root, x), os.getcwd()))
            if x in dirs:
                return(os.path.join(root, x), os.getcwd())

all__ = ['path_finder', 'filename']
if __name__ == "__main__":
    print(path_finder(filename()))
    open(path_finder(filename()))

