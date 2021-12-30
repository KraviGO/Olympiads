from math import ceil

T = input()
S = input()
N = int(input())

ans = 0
T_len = len(T)
S_len = len(S)
TS = ''.join([S[i % S_len] for i in range(S_len+T_len-1)])

for i in range(T_len + S_len):
    if TS[i:i+T_len] == T:
        ans += N - ceil((i+T_len) / S_len) + 1

print(max(ans, 0))
