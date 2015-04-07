class Deque(object):
    def __init__(self):
        self.items = []
        
    def add_rear(self, item):
        self.items.insert(0, item)
        
    def add_front(self, item):
        self.items.append(item)
    
    def remove_rear(self, item):
        return self.items.pop(0)
    
    def remove_front(self, item):
        return self.items.pop()
        
    def is_empty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)