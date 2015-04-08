def hash(a_string, table_size):
    sum = 0
    for pos in range(len(a_string)):
        sum = sum + (ord(a_string[pos]) * pos)
    return sum % table_size
    
    
print hash('kayak', 11)
print hash('kkaay', 11)