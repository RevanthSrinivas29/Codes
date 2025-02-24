n,h=map(int,input().split())
a=list(map(int,input().split()))
w=[]
for i in a:
    if i>h:
        w.append(2)
    else:
        w.append(1)
print(sum(w))
# n, h = map(int, input().split())
# a = list(map(int, input().split()))
# width = sum(2 if i > h else 1 for i in a)
# print(width)
