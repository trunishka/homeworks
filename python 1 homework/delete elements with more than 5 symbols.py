amount = ["asd", "asfbgs", "the one", "asdz", "adhcsf", "ertb", "gfdhg"]
new_amount = []
print(amount)
for i in amount:
    if len(i) < 5:
        new_amount.append(i)
amount=new_amount
print(amount)