# example
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# exercise a
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# exercise b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# exercise c
starQuantity = int(input("Enter number of stars: "))
for i in range (0, starQuantity, 1):
    print('*', end='')
print()

# exercise d
lineQuantity = int(input("Enter number of lines: "))
for i in range (1, lineQuantity+1, 1):
    for j in range(0, i, 1):
        print('*', end='')
    print()
