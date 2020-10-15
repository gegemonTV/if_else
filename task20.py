n, m, x, y = map(int, input().split())

if m > n :
    n, m = m, n

if x < m - x :
    s1 = x
else :
    s1 = m - x

if y < n - y :
    s2 = y
else :
    s2 = n - y

print(min(s1, s2))