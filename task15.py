a, b = map(int, input().split())

if a == b == 0 :
    print("INF")
elif (-b) % a != 0 :
    print("NO")
else :
    print((-b) // a)