k, m, n = map(int, input().split())

cook = n // k

if n % k != 0:
    cook += 1

cook = cook * m * 2

print(cook)