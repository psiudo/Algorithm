def solution(s):
    count = 0
    
    for ch in s:
        if ch == 'p' or ch == 'P':
            count += 1
        if ch == 'y' or ch == 'Y':
            count -= 1
    
    if count == 0:
        print("True")
        return True
    else:
        print("False")
        return False


