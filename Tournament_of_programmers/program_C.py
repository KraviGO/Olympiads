temp = float(input())
temp = float("{0:.1f}".format(temp))

print(temp)
if temp < 37:
    print('HEALTHY')
else:
    print('SICK')
