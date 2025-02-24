n,k=map(int,input().split())
c=0
l=list(map(int,input().split()))
for i in l:
    if i>k:
        c+=1
print(c)
  