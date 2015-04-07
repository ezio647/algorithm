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

string1 = "abcde"
stack_obj = Stack()
for a in string1:
    stack_obj.push(a)

    
# Once the characters from the string has been added to the stack.
#you can pop elements(in the reverse order) and add it to
#another Stack
#    OR
# a list 


# using STACK
rev_stack = Stack()
while stack_obj.size() >= 1 :    
    rev_stack.push(stack_obj.pop())
    

#using a LIST
    
rev_list = []

while stack_obj.size() >= 1 :
    rev_list.append(stack_obj.pop())
    
print rev_list   