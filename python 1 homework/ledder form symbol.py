__author__ = 'Trunishka'
user_in = input("insert the number of stairs")
try:
    number = int(user_in)
    for i in range (number):
        print(i * "*")
    else

except ValueError:
    print("insert only integer")
# надо отсечь отрицательные числа