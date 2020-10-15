x1, y1, x2, y2 = map(int, input().split())

dx = x1 - x2
dy = y1 - y2

if dx < 0 :
    dx = dx * (-1)

if dy < 0 :
    dy = dy * (-1)

if dx == dy :
    print("YES")
else :
    print("NO")
