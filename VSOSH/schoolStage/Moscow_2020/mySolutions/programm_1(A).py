K = int(input())
N = int(input())

left = N // K * K
right = (N // K + 1) * K

print(min(N-left, right-N))
