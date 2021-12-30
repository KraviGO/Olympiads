n = int(input())
k = int(input())

a = (k // (2*n + 1))
b = a * (2 * n + 1)

if k - b > 0:
    if (k-b) > n:
        print(a * 2 + 2, k-b-n)

    else:
        print(a * 2 + 1, k-b)

else:
    print(a * 2, n+1)
