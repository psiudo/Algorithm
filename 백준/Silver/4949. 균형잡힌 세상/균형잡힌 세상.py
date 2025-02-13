while True:
    line = input().rstrip()
    if line == ".":
        break
    stack_val = 0
    base = 3
    balanced = True
    for c in line:
        if c == '(':
            stack_val = stack_val * base + 1
        elif c == '[':
            stack_val = stack_val * base + 2
        elif c == ')':
            if stack_val % base != 1:
                balanced = False
                break
            stack_val //= base
        elif c == ']':
            if stack_val % base != 2:
                balanced = False
                break
            stack_val //= base
    print("yes" if balanced and stack_val == 0 else "no")
