from datetime import date, timedelta

def attcl(i, j):
    c = round((i / j) * 100, 2)
    diff = 3*j-4*i
    return c, diff

def clas_assign():
    b = []
    print('Enter the number of periods for each weekday (Mon-Sat), skipping Sunday:')
    for i in range(6):
        b.append(int(input(f"Day {i+1}: ")))
    return b

def Exctdate(b, res, i, j):
    dt = date.today()
    total = sum(b)
    pct = round(((res + i) / (res + j)) * 100, 2)

    while res >= total:
        dt += timedelta(days=7)
        res -= total

    day = dt.weekday()
    
    while res > 0:
        if day == 6:
            dt += timedelta(days=1)
            day = 0
        else:
            if res >= b[day]:  
                res -= b[day]
                dt += timedelta(days=1)
                day += 1
            else:
                break 

    dt += timedelta(days=1)
    return dt.strftime("%d, %B, %Y"), pct

if __name__ == '__main__':
    i = int(input('Enter attended periods count: '))
    j = int(input('Enter total periods held: '))

    if i == 0 or j == 0:
        print("Haven't the classes started yet?")
        exit(0)

    if (i / j) * 100 > 75:
        print(f'Your attendance is {round((i / j) * 100, 2)}%, which is above 75%.')
        exit(0)

    res1, res2 = attcl(i, j)
    print(f'Current attendance: {res1}%')
    print(f'You need to attend {res2} more classes (45 min per class) to reach 75% attendance.')

    if int(input('Enter 1 if you want to know the exact date: ')) == 1:
        b = clas_assign()
        result, percnt = Exctdate(b, res2, i, j)
        print(f'Expected date to reach 75% attendance: {result} -> {percnt}%')
