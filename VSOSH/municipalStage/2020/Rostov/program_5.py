x = input()
y = input()

deep = 0
I = x
for i in range(6):
    J = I
    for j in range(6):
        Z = J
        while int(Z[-1]) < 7:
            Y = Z
            while int(Y[0]) < 7:
                if Y == y:
                    print(deep)
                    exit()
                deep += 1
                Y = str(int(Y[0])+1) + Y[1:]
            Z = Z[:-1] + str(int(Z[-1])+1)
        J = J[1:] + J[0]
    I = I[-1] + I[:-1]