import os
srch_file = input("введите название фала")
x,y,z = (list(os.walk(".")))
for srch_file in x,y,z:
    print(srch_file)

print(x)
print(y)
print(z)