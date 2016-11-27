from sys import argv

result = {}
i = 0
#print(argv)

try: data_file = open(argv[1])
except:
    try: data_file = open(input ("Ведите путь и название файла"))
    except FileNotFoundError:
         data_file = open(input ("Ведите путь и название файла"))


counter = len(data_file.readlines())
data_file.seek(0)
def symbol_count():
    i = 0
    while i <= counter:
        line = data_file.readline()
        line = line.lower()
        line = line.rstrip()
        # print(line)
        elements = list(line)
        for element in elements:
            if element in result:
                result[element] += 1
            else:
                result[element] = 1
        i += 1
symbol_count()

data_file.close()

result_lst = sorted(result.values())
print(result_lst)


print(sorted(result.items()))


__all__= ['data_file','result', 'counter', 'result_lst', 'symbol_count']
