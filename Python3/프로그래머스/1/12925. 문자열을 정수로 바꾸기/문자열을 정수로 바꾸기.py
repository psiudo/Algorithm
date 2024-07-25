def solution (s):
    result = 0
    sign = 1
    
    if s[0]=='-':
        sign = -1
        s=s[1:]
    elif s[0]=='+':
        sign = +1
        s=s[1:]
        
    for char in s:
        result = result*10+(int(char))
    
    return sign*result