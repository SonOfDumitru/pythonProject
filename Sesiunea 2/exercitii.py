x = int(input('x: '))

# 3


if x > 0:
    print('x e numar pozitiv')
elif x == 0:
    print('x e numar')
else:
    print('x e negativ')

# 4

print(-2 <= x <= 16)

# 5

y = int(input('y: '))
z = x - y
if x > y and z <= 5:
    print(' diferența dintre x și y este mai mică de 5')
elif x < y:
    print('numar negativ')
else:
    print('diferenta mare')

# 6
if y > 5 and y > 25:
    if x != y:
        print(x is not y)
else:
    print( x is y)

#7

if x==y:
    print('egale')
elif x>y:
    print('x mai mare')
else:
    print('y mai mare')


# 2

if type(x)==int and x>0:
    print('x este numar natural')
else:
    print('x este nenatural')

