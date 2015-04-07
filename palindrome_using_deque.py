from deque import Deque

def palindrome_check(word):
    letter_deque = Deque()
    for w in word:
        letter_deque.add_rear(w)
        
    status = True
    
    while letter_deque.size()> 1 and status:
        first_letter = letter_deque.remove_rear()
        last_letter = letter_seque.remove_front()
        
        if first_letter != last_letter:
            status = False
            
        return status
        
print(palindrome_check("lsdkjfskf"))
print(palindrome_check("radar"))