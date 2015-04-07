
import time
"""
def sum_of_n_2(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i
    end = time.time()
    return the_sum,end-start
    

print("Sum is %d required %10.7f seconds" % sum_of_n_2(10000))
print("Sum is %d required %10.7f seconds" % sum_of_n_2(100000))

"""
def sum_of_n_3(n):
    start = time.time()
    the_sum = (n * (n + 1)) / 2
    end = time.time()
    return the_sum,end-start

print("Sum is %d required %15.14f seconds" % sum_of_n_3(10000))
print("Sum is %d required %15.14f seconds" % sum_of_n_3(100000))


a = 5
b = 6
c = 10
for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j
for k in range(n):
    w = a * k + 45
    v = b * b
d = 33

t(n) = 3 + 3n2 + 2n