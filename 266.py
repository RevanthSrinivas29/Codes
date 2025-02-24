n=int(input())
c=0
a=input()
for i in range(n-1):
    if a[i]==a[i+1]:
        c+=1
print(c)
