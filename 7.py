n = int(input("Введіть число n: "))
m = 1

for a in range(-n, n, m):
    if a % 2 == 0:
        print(a)
