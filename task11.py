x1, y1, x2, y2 = map(int, input().split())

dx = x1 - x2
dy = y1 - y2

if dx < 0 :
    dx = -dx

if dy < 0 :
    dy = -dy

if dx == dy :
    print("YES")
elif x1 == x2 or y1 == y2 :
    print("YES")
else :
    print("NO")
