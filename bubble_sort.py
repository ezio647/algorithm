def bubble_sort(num_list):
    length = len(num_list)
    
    for i in range (0, length):
        flag = 0
        for j in range (0, length - 1):
            if num_list[j] > num_list[j + 1] :
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]        
    return num_list
      
#num = [1, 2, 3, 4,5]                      
num = [4, 3, 2, 5,1]                      
bubble_sort(num)
print num