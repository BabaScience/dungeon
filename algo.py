
count = 0
i = 0
for a in range(0, 1000):
    for b in range(0, 1000):
        for c in range(0, 1000):
            count += 1
            i += 1
            if a/10 + b/10 == 8.0 and a/10 + c/10 == 13.0 and c/10 - a/10 == 6.0:
                print('a ->', a/10, 'b ->', b/10, 'c ->', c/10)
                print('i ->',i)

print('Programme terminé')
print('count: ', count)