#The program has 4 different functions that generate
# list of numbers 0 - n
def test1(): # using concatenation
    l = []
    for i in range(1000):
        l = l + [i]
        
def test2(): # through append
    l = []
    for i in range(1000):
        l.append(i)
         
def test3(): # list comprehension
    l = [i for i in range(1000)]
    
def test4(): #wrapping range oprator with list constructor
    l = list(range(1000))
    
import timeit #import timeit module
from timeit import Timer     #import timer class


t1 = Timer("test1()", "from __main__ import test1")
print "concat", t1.timeit(number = 1000), " milliseconds"

t2 = Timer("test2()", "from __main__ import test2")
print "append", t2.timeit(number = 1000), "milliseconds"

t3 = Timer("test3()", "from __main__ import test3")
print "list comprehension", t3.timeit(number = 1000), "milliseconds"

t4 = Timer("test4()", "from __main__ import test4")
print "list(range)", t3.timeit(number = 1000), "milliseconds"