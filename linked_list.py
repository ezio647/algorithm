class Node:
    """ A class that creats linked  list nodes"""
    def __init__(self, init_data):  # intialize list
        self.data = init_data   #assign the value in the parameter to data field 
        self.next = None   #set the address intially to none
        
    def get_data(self):   # returns the element stored in the node.
        return self.data  
        
    def get_next(self):      #returns the address of the next node.
        # It will be None if it is single element list
        return self.next
        
    def set_data(self, new_data):  # sets the value of the node to the parameter
        self.data = new_data  
         
    def set_next(self, new_next):  # sets the address to the address of the next node.
        self.next = new_next
        
class UnorderdList():
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
        
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    
    def size(self):
        length = 0
        current = self.head   # current  holds the address where head points to.
        while current != None : # while the address of next item is not None
            length += 1
            current = current.get_next()  #set current address to point to next element

        return length
        
    def search(self, key):
        is_found = False
        current = self.head
        
        while current != None and is_found == False:
            if current.data == key:
                is_found == True
            else:
                current = current.get_next()
        return is_found       
        
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        
        while current != None and found == False:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.get_next()
                
        if previous == None:
            self.head = current.get_next()
            
        elif current == None:
            print "element not present"
            
        else:
            previous.set_next(current.get_next())
           
    def display(self):
        current = self.head
        while current != None:
            print current.data
            current = current.get_next()
            
"""        
temp = Node(93)
print temp.get_data()    
print temp.get_next()       
"""

ul = UnorderdList()
ul.add(1)
ul.add(2)
ul.add(3)
ul.add(4)
ul.add(5)
ul.add(6)
ul.add(1)
ul.add(2)
ul.add(3)
ul.add(4)
ul.add(5)
ul.add(6)
ul.display()
print "Remove called"
ul.remove(5)
ul.display()
