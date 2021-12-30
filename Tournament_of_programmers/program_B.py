h = int(input())
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    h -= x*y

if h > 0:
    print('is alive')
else:
    print('is dead')
