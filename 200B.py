n=int(input())
p=list(map(int,input().split()))

vol=sum(p)/n
print(vol if n>0 else 0)