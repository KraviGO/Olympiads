def OK_(a, x):
    global s, t
    ost = s
    for i in range(t):
        ost = max(ost + a[i] - x, 0)
    return not ost


s = int(input())
t = int(input())
a = [int(input()) for _ in range(t)]

L = -1
R = int(2e9)
while R - L > 1:
    m = (L + R) // 2
    if OK_(a, m):
        R = m
    else:
        L = m

print(R)