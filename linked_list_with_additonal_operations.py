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

    def append_list(self, item):
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
            
        temp = Node(item)
        current.set_next(temp)
 
            
                                              
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

    def index(self, key):
        index_of_key = 0
        current = self.head
        while current != None:
            if current.data == key :
                return index_of_key
            else:
                  current = current.get_next()
                  index_of_key += 1  
        return None
    
    def insert(self, ind, item):
        current = self.head
        previous = None
        position = 0
        if ind == 0:
            temp = Node(item)
            temp.set_next(current)
            self.head = temp
            return
            
        while current != None:
            if ind == position:
                break
            elif item != position:
                position += 1
                previous = current
                current = current.get_next()
        
        print "position value:",position
        if ind <= position :
            temp = Node(item)
            temp.set_next(current)
            previous.set_next(temp)
        else:
            print "Out of index error"
   
    def pop(self, *pos):
        index = 0
        previous = None
        current = self.head
        popped_element = None
        stop = False
        if len(pos) < 1 :
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            print " pop()"     
            popped_element  =  current.get_data()
            previous.set_next(current.get_next())
            return popped_element
        pos = pos[0]
        if pos == 0:
            popped_element = current.data
            current =(current.get_next())
            self.head = current 
            return popped_element
                          
        if pos > ul.size():
            print "Out of index error"
            return None
        

            
        while current != None and stop == False :
            if pos != index:
                index += 1
                previous = current
                current = current.get_next()
            else:
                stop = True
                
        if pos == index:
            popped_element = current.data
            previous.set_next(current.get_next())
            return popped_element
            
              
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
#print "first element added"

ul.add(1)
ul.add(2)
ul.add(3)
ul.add(4)
ul.add(5)
ul.add(6)

print "display called"
ul.display()

#Append test
#ul.append_list(7)
#print "After appending 7"
#ul.display()

#Remove test
#print "Remove called"
#ul.remove(5)
#ul.display()

#Index test - This method takes an argument(key). If key is present , it returns the index of the key. Else prints an appropriate message.
#print "index of 4",ul.index(4)

#pop test
#print "Pop called"
#print "Popped element:",ul.pop()
#print "After pop"
#ul.display()

# Insert test- Accepts two arguments(index, item). If index <len then allow insert.
# test 1: index out of range
#test2: index = 0
#test3:index = last
#test4:index = middle
ul.insert(4, 7)
print "After inserting "
ul.display()