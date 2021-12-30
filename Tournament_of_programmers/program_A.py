x, y, z = [int(input()) for i in range(3)]

if x + y + z < 3:
    print(x+y+z)
else:
    print((x+y+z) % ((x+y+z)//3))
