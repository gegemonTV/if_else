n, m, k = map(int, input().split())

print("YES" if (((k // n < m) and (k % n == 0)) or ((k // m < n) and (k % m == 0))) else "NO")