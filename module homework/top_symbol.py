import os
from sys import argv


def top_symbol(x):
    result = {}
    data_file = x
    with open(data_file) as data_file:
        counter = len(data_file.readlines())
        data_file.seek(0)
        i = 0
        while i <= counter:
            line = data_file.readline()
            line = line.lower()
            line = line.rstrip()
            elements = list(line)
            for element in elements:
                if element in result:
                    result[element] += 1
                else:
                    result[element] = 1
            i += 1

        result.pop(" ")
        result_lst = sorted(result.values())
        result_lst.reverse()

    for ltr, frq_num in result.items():
        if frq_num == result_lst[0]:
            return ltr,frq_num


def filename():
    if len(argv) > 1:
        file_name = argv[1]
    else:
        file_name = input("insert the name")
        while file_name not in os.listdir():
            file_name = input("insert the name")
    return file_name

__all__ = ['top_symbol']
if __name__ == "__main__":
   print(top_symbol(filename()))



