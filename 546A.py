k,n,w=map(int,input().split())
l=0
for i in range(1,w+1):
    l+=i*k
m=l-n
if m>0:
    print(m)
else:
    print(0)