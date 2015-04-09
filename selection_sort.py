def selection_sort(num_list):
    length = len(num_list)
    for i in range (0, length):
        min = i
        for j in range(i + 1 , length):
            print "comparing", num_list[j], "and", num_list[min]
            if  num_list[j] < num_list[min]:
                min = j
                       
        num_list[i], num_list[min] = num_list[min], num_list[i]
            
    return num_list
    
num = [4, 3, 7,5,1,2]
selection_sort(num)
print num