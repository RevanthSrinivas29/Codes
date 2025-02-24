matrix = [list(map(int, input().split())) for _ in range(5)]
c = 0

for r in range(5):
    if 1 in matrix[r]:
        o = matrix[r].index(1) + 1
        p = [r + 1, o]
        break

while p[0] < 3:
    p[0] += 1
    c += 1
while p[0] > 3:
    p[0] -= 1
    c += 1
while p[1] < 3:
    p[1] += 1
    c += 1
while p[1] > 3:
    p[1] -= 1
    c += 1

print(c)
