def bubble_sort1(num_list):
    length = len(num_list)
    num_loop = 0
    for i in range (0, length):  # responsible for each pass
        flag = 0
        for j in range (0, length - 1): # responsible for comparing consecutive elements in each pass
            if num_list[j] > num_list[j + 1] :
                print "comparing", num_list[j], "and ", num_list[j +1]
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]    

    return num_list
    
# This is the improved bubble_sort function. This detects whether a swap has been made during a pass. 
# If no swap has been made, the list is already sorted and the algorithm can stop.

def bubble_sort2(num_list):
    length = len(num_list)
    swap = True
    i = 0
    while i < length and swap:
        swap = False
    for i in range (0, length):
        flag = 0
        for j in range (0, length - 1):
            if num_list[j] > num_list[j + 1] :
                swap = True
                print "comparing", num_list[j], "and ", num_list[j +1]
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]    

    return num_list

      
            
def bubble_sort3(num_list):
    length = len(num_list)
    flag = 0
    for i in range (0, length):  # responsible for each pass
        flag = 0
        for j in range (0, length - 1): # responsible for comparing consecutive elements in each pass
            if num_list[j] > num_list[j + 1] :
                flag = 1
                print "comparing", num_list[j], "and ", num_list[j +1]
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]    
        if flag == 1:
            continue
    return num_list
    
                                                    
#num = [1, 2, 3, 4,5]                      
num = [4, 3, 7,2, 5,1]                      
bubble_sort(num)
print num