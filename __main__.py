def bool_rep(n):
    if n == 0:
        return []
    else:
        return bool_rep(n // 2) + [n % 2]

n = 3000
print(bool_rep(n))  # Output: [1, 0, 1]