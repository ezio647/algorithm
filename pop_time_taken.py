import timeit #import timeit module
from timeit import Timer     #import timer class

pop_zero = Timer("x.pop(0)","from __main__ import x")

pop_end = Timer("x.pop()","from __main__ import x")

x = list(range(2000000))

print pop_zero.timeit(number=1000)
print pop_zero.timeit(number=1000)

x = list(range(2000000))

print pop_end.timeit(number=1000)
print pop_end.timeit(number=10000)