n=int(input())
x=0
for i in range(n):
    a=input()
    if a=='++X' or a=='X++':
        x+=1
    if a=='--X' or a=='X--':
        x-=1
print(x)
