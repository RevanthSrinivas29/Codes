n=int(input())
s=str(input())
a=s.count('A')
b=s.count("D")
print('Anton' if a > b else 'Danik' if b > a else 'Friendship')