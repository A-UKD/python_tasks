n = int(input())
m = int(input())

for a in range(-n, n, m):
    if a % 2 == 0:
        print(a)
