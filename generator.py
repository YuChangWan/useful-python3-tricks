def generator1():
    for i in range(10):
        yield i


g1 = generator1()
for i in g1:
    print(i,end=' ')

print()
g2 = (x for x in range(10))
for i in g2:
    print(i, end=' ')

print()
for i in (x for x in range(10)):
    print(i, end=' ')
