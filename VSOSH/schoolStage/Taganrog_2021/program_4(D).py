xEl = int(input())
yEl = int(input())
xFin = int(input())
yFin = int(input())

if (xEl + yEl) % 2 == (xFin + yFin) % 2:
    print('Yes')

    x1 = ((yFin + xFin) - (yEl - xEl)) // 2
    y1 = x1 + (yEl - xEl)

    x2 = ((yEl + xEl) - (yFin - xFin)) // 2
    y2 = x2 + (yFin - xFin)

    if x1 == xFin and y1 == yFin:
        print(1)
        print(xFin, yFin)
    else:
        print(2)
        if (1 <= x1 <= 8) and (1 <= y1 <= 8):
            print(x1, y1)
        else:
            print(x2, y2)

        print(xFin, yFin)

else:
    print('No')
