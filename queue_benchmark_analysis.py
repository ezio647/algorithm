class Queue(object):
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
        
    def is_empty(self):
        return self.items == []
        
    def size(self):
        return size(self.items)
    
    def display(self):
        print self.items
"""   
q = Queue()
q.enqueue(3)
q.enqueue('hello')
q.enqueue('dog')
q.dequeue()
q.display()
"""
q = Queue()

import timeit #import timeit module
from timeit import Timer     #import timer class

t1 = Timer("Queue.enqueue(3)", "from __main__ import Queue.enqueue")
print "q.enqueue(3", t1.timeit(number = 1000), " milliseconds"
