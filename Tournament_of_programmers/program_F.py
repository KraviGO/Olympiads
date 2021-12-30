n = int(input())
S = input()
l = int(input())
r = int(input())

a = ((r+1) // n) * S.count('a')
b = S[l:(r+1) % n].count('a')
print(a+b)