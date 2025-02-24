n = int(input())
k_odd = (n + 1) // 2
k_even = n // 2

result = k_even * (k_even + 1) - k_odd * k_odd
print(result)
