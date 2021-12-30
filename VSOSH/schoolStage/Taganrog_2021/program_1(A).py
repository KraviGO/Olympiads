n = int(input())
d = int(input())

print(max((n - (7-d+1) % 7) // 7, 0))
