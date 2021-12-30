n = int(input())

ans = 0
num = 0
for i in range(61):
    for j in range(37):
        for z in range(27):
            num = 2**i * 3**j * 5**z
            if ans < num <= n:
                ans = num

print(ans)
