a, b, c, d, e = map(int, input().split())

if a > b :
    a, b = b, a
if a > c :
    a, c = c, a
if b > c :
    b, c = c, b

if e > d :
    d, e = e, d

if d >= b and e >= a :
    print("YES")
else :
    print("NO")