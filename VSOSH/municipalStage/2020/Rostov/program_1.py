from math import ceil

a, b, c = [int(input()) for _ in range(3)]

# 7 class
cupe_7 = ceil(a / 4)
teachers = ceil(cupe_7 / 3)

# 8 class
cupe_8 = ceil(b / 4)
teachers += ceil(cupe_7 / 2)

# 9 class
cupe_9 = ceil(c / 4)
teachers += cupe_9

print((cupe_7 + cupe_8 + cupe_9) * 4, teachers)