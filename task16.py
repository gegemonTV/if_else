n = int(input())

cow_str = "коров"

if n % 10 == 1 :
    cow_str += 'а'
if 2 <= n % 10 <= 4 :
    cow_str += 'ы'

print(n, cow_str)