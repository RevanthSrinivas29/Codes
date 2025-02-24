a=str(input())
c,d=0,0
for i in a:
    if i.islower():
        c+=1
    elif i.isupper():
        d+=1
if c>=d:
    print(a.lower())
else:
    print(a.upper())