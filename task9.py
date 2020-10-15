x1, y1, x2, y2 = map(int, input().split())

if (-1 <= (x1 - x2) <= 1) and (-1 <= (y1 - y2) <= 1) :
    print("YES")
else :
    print("NO")
