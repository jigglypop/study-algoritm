word = 0
for i in range(1, 21):
    word |= (1 << i)
print(word)