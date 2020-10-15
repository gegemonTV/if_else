x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

if x1 <= x3 <= x2 and y1 <= y3 <= y2 :
    print("YES")
elif x1 <= x4 <= x2 and y1 <= y4 <= y2 :
    print("YES")
else :
    print("NO")