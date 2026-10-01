n = 15
center = n // 2
for i in range (n):
    row = ["*" if i == center or j == center or i == j or i + j == n - 1 else "." for j in range(n)]
    print("".join(row))
