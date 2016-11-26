from sys import argv

result = {}
i = 0
#print(argv)
data_file = open(argv[1])
counter = len(data_file.readlines())
data_file.seek(0)

while i <= counter:
    line = data_file.readline()
    line = line.lower()
    line = line.rstrip()
    print(line)
    elements = list(line)
    for element in elements:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    i += 1
result_lst = list(result.values())
result_lst = result_lst.sort()
print(result_lst)


print(sorted(result.items(), key = result_lst, reverse = True))
# for result_lst in sorted(result.values()):
#     print(result_lst)
#           # ":", result.values())