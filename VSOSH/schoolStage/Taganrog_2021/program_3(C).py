n = int(input())

mas = []
set_mas = set()
ans = 0
for i in range(n):

    l = int(input())
    mas.append(l)
    set_mas.add(l)

    if len(mas) == 3 and len(set_mas) == 1:
        ans += 1
        mas = []
        set_mas = set()

    if len(set_mas) > 1:
        mas = [l]
        set_mas = set()
        set_mas.add(l)

print(ans)
