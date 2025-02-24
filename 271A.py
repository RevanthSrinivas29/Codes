n=input()
n=str(int(n)+1)
b=set(n)
k=int(n)
while len(n)!=len(b):
    k+=1
    b=set(str(k))
print(k)