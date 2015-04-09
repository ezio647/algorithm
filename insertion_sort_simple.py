def insert_sort(num_list):
    length = len(num_list)
    for i in range(1, length):
        j = i
        while j > 0 and num_list[j] < num_list[j - 1]:
            num_list[j] , num_list[j-1] = num_list[j-1], num_list[j]
            j= j - 1
            
    return num_list
    
num = [4, 5, 2, 7, 1]
insert_sort(num)
print num
        