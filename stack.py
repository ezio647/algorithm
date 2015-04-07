class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[-1]
        
    def size(self):
        return len(self.items)
        
       
new_stack = Stack()
print new_stack.is_empty()
new_stack.push(4)
new_stack.push('dog')
print new_stack.peek()
print(new_stack.size())
print(new_stack.is_empty())
new_stack.push(8.4)
print(new_stack.pop())
print(new_stack.pop())
print(new_stack.size())
