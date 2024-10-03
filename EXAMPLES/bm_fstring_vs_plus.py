import os
import timeit
y = "John"
x = "Strickler"
null = open(os.devnull, "w")

t1 = timeit.timeit("print(f'My name is {y} {x}', file=null)", setup="from __main__ import x,y,null", number=1000000)
# 4.74 s

t2 = timeit.timeit("print('My name is', y, x, file=null)", setup="from __main__ import x,y,null", number=1000000)

t3 = timeit.timeit("print('My name is' + y + x, file=null)", setup="from __main__ import x,y,null", number=1000000)

t4 = timeit.timeit("print('My name is {} {}'.format(y, x), file=null)", setup="from __main__ import x,y,null", number=1000000)

t5 = timeit.timeit("print('My name is %s %s' % (y, x), file=null)", setup="from __main__ import x,y,null", number=1000000)

for x in t1, t2, t3, t4, t5:
    print(f"{x = }")

