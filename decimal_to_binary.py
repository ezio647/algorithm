#import stack
from stack import Stack

def dec_to_bin(dec_number):
    rem_stack = Stack()
    
    while dec_number > 0:
        remainder = dec_number % 2
        rem_stack.push(remainder)
        dec_number = dec_number // 2
        
    binary_string = ""
    while not rem_stack.is_empty():
        binary_string += str(rem_stack.pop())
        
    return binary_string
    
print dec_to_bin(233)
         
    