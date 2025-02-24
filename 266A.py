n, t = map(int, input().split())
s = list(input())
l=[]
for _ in range(t):
    for i in range(len(s) - 1):
        if s[i] == 'B' and s[i + 1] == 'G':
            l[i], l[i + 1] = s[i + 1], s[i]
            i += 1
s = ''.join(l)
print(s)
