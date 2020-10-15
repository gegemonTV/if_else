n = int(input())

six = n // 60
n = n - (six * 60)
ten = n // 10
n = n - (ten * 10)

if n * 15 > 125 :
    ten = ten + 1
    n = 0

if ten * 125 > 440 :
    six = six + 1
    ten = 0

print(n, ten, six)