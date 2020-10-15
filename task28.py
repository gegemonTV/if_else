h1, w1, h2, w2 = map(int, input().split())

if w1 > h1 :
    w1, h1 = h1, w1

if w2 > h2 :
    w2, h2 = h2, w2

height = max(h1, h2)

width = 0

if max == h1 :
    if h2 > w1 :
        h2, w1 = w1, h2
    if h2 > w2 :
        h2, w2 = w2, h2
    if w1 > w2 :
        w1, w2 = w2, w1

    width = h2 + w1
else :
    if h1 > w1 :
        h1, w1 = w1, h1
    if h1 > w2 :
        h1, w2 = w2, h1
    if w1 > w2 :
        w1, w2 = w2, w1

    width = h1 + w1

print(height, width)