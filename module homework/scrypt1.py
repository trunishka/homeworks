from sys import argv

result = {}

#print(argv)

def top_symbol():
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
    result.pop(" ")
    result_lst = sorted(result.values())
    result_lst.reverse()
    # print(result_lst)
    for ltr, frq_num in result.items():
        if frq_num == result_lst[0]:
            return (ltr)

    # print(sorted(result.items()))
if __name__ == "__main__":
    top_symbol()

__all__= ['top_symbol', "result"]
