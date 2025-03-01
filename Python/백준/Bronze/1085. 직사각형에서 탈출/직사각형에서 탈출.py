x, y, w, h = map(int, input().split())

if x <= w/2 : 
    dx = x
elif x > w/2 :
    dx = w - x

if y <= h/2 :
    dy = y
elif y > h/2 :
    dy = h - y

print(min(dx, dy))