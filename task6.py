a, b, c = map(int, input().split())

res = (a == b) + (b == c) + (a == c)

if res != 3 :
    res = res + 1

print(res)
