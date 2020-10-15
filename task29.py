n = int(input())

res = ''

res = res + ('M' * (n // 1000))

n = n % 1000
tmp = n // 100

if tmp < 4 :
    res = res + ('C' * tmp)
elif tmp == 4 :
    res = res + "CD"
elif 5 <= tmp < 9 :
    res = res + 'D' + ('C' * (tmp - 5))
else :
    res = res + "CM"

n = n % 100
tmp = n // 10

if tmp < 4 :
    res = res + ('X' * tmp)
elif tmp == 4 :
    res = res + "XL"
elif 5 <= tmp < 9 :
    res = res + 'L' + ('X' * (tmp - 5))
else :
    res = res + "XC"

n = n % 10
tmp = n

if tmp < 4 :
    res = res + ('I' * tmp)
elif tmp == 4 :
    res = res + "IV"
elif 5 <= tmp < 9 :
    res = res + 'V' + ('I' * (tmp - 5))
else :
    res = res + "IX"

print(res)