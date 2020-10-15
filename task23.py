a, b, c, an, bn, cn = map(int, input().split())

if a > b :
    a, b = b, a
if a > c :
    a, c = c, a
if b > c :
    b, c = c, b

if an > bn :
    an, bn = bn, an
if an > cn :
    an, cn = cn, an
if bn > cn :
    bn, cn = cn, bn

print((c // cn) * (b // bn) * (a // an))