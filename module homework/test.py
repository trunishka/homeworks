import random
d = dict((i, random.randint(0, 100)) for i in range(5))
l = lambda x: x[1]

print( sorted(d.items(), key=l, ))#reverse=True) )

sorted