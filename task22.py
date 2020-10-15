a1, b1, c1, a2, b2, c2 = map(int, input().split())

if a1 > b1 :
    a1, b1 = b1, a1
if a1 > c1 :
    a1, c1 = c1, a1
if b1 > c1 :
    b1, c1 = c1, b1

if a2 > b2 :
    a2, b2 = b2, a2
if a2 > c2 :
    a2, c2 = c2, a2
if b2 > c2 :
    b2, c2 = c2, b2

if a1 == a2 and b1 == b2 and c1 == c2 :
    print("Boxes are equal")
elif max(a1, a2) == a1 and max(b1, b2) == b1 and max(c1, c2) == c1 :
    print("The first box is larger than the second one")
elif max(a1, a2) == a2 and max(b1, b2) == b2 and max(c1, c2) == c2 :
    print("The first box is smaller than the second one")
else :
    print("Boxes are incomparable")