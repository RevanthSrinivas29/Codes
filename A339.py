a=list(input().strip())
for i in range(0,len(a)-2,2):
    for j in range(len(a)-2):
        if a[j]>a[j+2]:
            a[j],a[j+2]=a[j+2],a[j]
b=a = "".join(map(str, a))
print(b)
    