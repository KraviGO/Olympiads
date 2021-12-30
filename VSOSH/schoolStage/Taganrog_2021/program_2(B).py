n1 = int(input())
n2 = int(input())

if n2 % 2:
    if n1 >= 2 and n1 % 2 == 0:
        print('YES')
        print((n1-2) // 2, (n2 // 2 + 1))
    else:
        print('NO')

else:
    if n1 % 2 == 0:
        print('YES')
        print(n1 // 2, n2 // 2)
    else:
        print('NO')
