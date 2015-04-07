class Queue(object):
    def __init__(self):
        self.items = []
        
#    def enqueue(self, item):  #This inserts the element at the front of the list
#        self.items.insert(0, item)

    def enqueue(self, item):
        self.items.append(item)
                                
#    def dequeue(self):  # This removes from the end of the end of the list
#        return self.items.pop()

    def dequeue(self):
        return self.items.pop(0)
                    
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