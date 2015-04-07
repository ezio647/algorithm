#This calculates the time taken for finding minimum number in a list
#where the time complexity of the algorithm is O(n2) and O(n)

import time
import random

def minimum(list_of_num, n): #this function has a time complexity of O(n2)
    start = time.time()
    min = list_of_num[0]
    for i  in range(0, n - 1):
        for j in range(i + 1, n):
            if list_of_num[j] < min:
                min = list_of_num[j]
    end = time.time()            
    return min, end-start

def minimum2(list_of_num, n):  #this function has a time complexity of O(n)
    start = time.time()
    min = list_of_num[0]
    for i in range(1, n):
        if list_of_num[i] < min:     
            min = list_of_num[i]
            
    end = time.time()
    return min, end-start
    
    
#num = [5, 3, 33, 8, 6, 91,200]
random_list = random.sample(xrange(1,100), 90)#gets random list of numbers in the range 0-100
    

print("Min is %d required %15.14f seconds" % minimum(random_list, len(random_list)))
print("Min is %d required %15.14f seconds" % minimum2(random_list, len(random_list)))

#Clearly the funciton that has O(n) i.e. minimum2 takes less time.