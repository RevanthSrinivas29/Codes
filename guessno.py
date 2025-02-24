from random import randint
ans=randint(0,100)
print('Number Guessing--\nYou have total 10 chances' )
guess=int(input('Guess a no. from 1 to 100:'))
l=['Your guess is correct','super duper close','Super close','Try hard ! You are close enough ','just in reach','Close enough']
n=10
while n!=0:
    if guess==ans:
        print(l[0])
        exit(0)
    else:
        diff=(ans-guess)*(-1) if ans-guess<0 else ans-guess
        if diff<=10:
            print(l[diff] if diff<=5 else 'You are so close')
        else:
            print(f'not close enough ')
        guess=int(input(f'You have total {n} chances left:'))
        n-=1
print(f'You lose BOT\nNumber is {ans}')
