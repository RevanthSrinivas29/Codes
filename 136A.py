n=int(input())
a=input().split()
c=1
l=[0 for i in range(n)]
for i in a:
    k=int(i)
    l[k-1]=c
    c+=1
l=' '.join(map(str,l))
print(l)