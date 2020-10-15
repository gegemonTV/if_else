a, b, c = map(int, input().split())

if a < c > b :
    a, c = c, a

if a < b > c :
    a, b = b, a

if a > b + c :
    print("Impossible")
elif a * a == b * b + c * c :
    print("Rectangular")
elif a * a > b * b + c * c :
    print("Obtuse")
else :
    print("Acute")