import array as a

def binsearch(low,high,l,b):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==b:
             return f'element found at {mid+1}'
        elif b<l[mid]:
            high=mid-1
        else:
            low=mid+1
    return 'element not found'

n=int(input("emter size of array:"))
l=a.array('i',[int(input()) for b in range(n)])
low,high=0,n-1
b=int(input("enter element to search:"))
print(binsearch(low,high,l,b))


            