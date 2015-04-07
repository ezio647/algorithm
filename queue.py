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
        
q = Queue()
q.enqueue(3)
q.enqueue('hello')
q.enqueue('dog')
q.dequeue()
q.display()