t=int(input())
l=[]
while t!=0:
    n=int(input())
    out=0
    a=input().replace(' ','')
    mid=n//2
    s1=a[:mid]
    s2=a[mid:]
    for i in s1:
        if i in s2:
            out+=1
    l.append(out)
    t-=1
k='\n'.join(map(str,l))
print(k)