def binary_search(num_list, key):
    first = 0
    last = len(num_list )- 1
    mid = (first + last )/2
    found = False
    while first <= last and not found:
        mid = (first + last )/2
        if num_list[mid] == key:
            found = True
        else :
            if key < num_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
            
        return found
        
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))