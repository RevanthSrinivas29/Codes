n=int(input())
a=list(map(int,input().split()))
f=True
for i in a:
    if i==1:
       f=False
       break
print('EASY' if f else 'HARD')
