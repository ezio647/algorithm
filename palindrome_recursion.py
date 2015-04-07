# -*- coding: utf-8 -*-
def fun_pal(phrase):
    is_pal = False
    print phrase
    if len(phrase) <= 1:
        print "len = 1 block"
        return True
   
    elif phrase[0] == phrase[-1]:
        return fun_pal(phrase[1:-1])
    
    else:
        print "else"
        #is_pal = False
        return False
        
    return is_pal

s = "k"    
print fun_pal(s)

"""
kayak
aibohphobia
Live not on evil
Reviled did I live, said I, as evil I did deliver
Go hang a salami; I’m a lasagna hog.
Able was I ere I saw Elba
Kanakanak – a town in Alaska
Wassamassaw – a town in South Dakota
"""