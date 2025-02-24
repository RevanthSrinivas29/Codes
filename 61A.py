a=input()
b=input()
i=0
s=''.join(['1' if a[i]!=b[i] else '0' for i in range(len(a))])
print(s)
# while i<len(a):
#     print(a[i])
#     if a[i]!=b[i]:
#         s+='1'
#     else:
#         s+='0'
#     i+=1
