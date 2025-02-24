a = int(input())
c = 0

while a > 0:
    if a >= 5:
        a -= 5
    elif a >= 4:
        a -= 4
    elif a >= 3:
        a -= 3
    elif a >= 2:
        a -= 2
    elif a >= 1:
        a -= 1
    c += 1

print(c)
