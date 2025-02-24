n = input()
count = sum(1 for digit in n if digit in '47')
print('YES' if count == 4 or count == 7 else 'NO')
