line = str(input("insert data"))
length = len(line)
total = 0
for i in range(length):
    x = line[i]
    try:
        res = int(x)
        total += res
    except:
        continue
print(total)
