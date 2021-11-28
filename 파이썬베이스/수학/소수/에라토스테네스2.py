m, n = 3, 16
check = [False] * (n + 1)
check[0] = check[1] = True

for i in range(2, (n + 1)):
    if not check[i]:
        j = i + i
        while j < (n + 1):
            check[j] = True
            j += i

for i in range(m, n+1):
    if check[i] == False:
        print(i)
print(check)