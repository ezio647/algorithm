def fun_pal(phrase):
    is_pal = False
    print phrase
    if len(phrase) <= 1:
        print "len = 1 block"
        return True
        
        print "after return"
    
    elif phrase[0] == phrase[-1]:
        fun_pal(phrase[1:-1])
    
    else:
        print "else"
        return False
        
    return is_pal

s = "kayak"    
print fun_pal(s)