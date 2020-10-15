x1, y1, x2, y2 = map(int, input().split())

dx = x1 - x2
dy = y1 - y2

if dx < 0 :
    dx = -dx

if dy < 0 :
    dy = -dy

if dy == 2 and dx == 1 :
    print ("YES")
elif dy == 1 and dx == 2 :
    print ("YES")
else :
    print ("NO")
