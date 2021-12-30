x = int(input())
y = int(input())

if not (x+y) % 2:

    if x > y:
        if abs(x) > abs(y):
            x0 = (x+y) // 2
            print(1)
            print(x0, x0, 'H')

        elif y < x <= abs(y):
            x2 = x - y
            x1 = x2 // 2
            print(2)
            print(x2, 0, 'V')
            print(x1, x1, 'H')

    elif x < y:
        if abs(x) < abs(y):
            x0 = (x + y) // 2
            print(1)
            print(x0, x0, 'V')

        elif x < y <= abs(x):
            y2 = y - x
            y1 = y2 // 2
            print(2)
            print(0, y2, 'H')
            print(y1, y1, 'V')

    else:
        if 0 < x <= y:
            print(0)
        else:
            print(3)
            y3 = x + y
            x2 = -y3
            x1 = x2 // 2
            print(0, y3, 'H')
            print(x2, 0, 'V')
            print(x1, x1, 'H')

else:
    print(-1)
