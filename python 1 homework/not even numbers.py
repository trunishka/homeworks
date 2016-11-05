__author__ = 'Trunishka'
users_number = input("insert number")
try:
    number = int(users_number)
    if type(number)== int:
        for i in range(number):
            if i % 2 != 0:
                print("not even numbers =", i)
                i += 1
        for i in range(number):
            if i % 2 == 0:
                print("even numbers = ", i)
                i +=1
except ValueError:
    print("insert only integer")

print('Finish')
