# 1. if

a = 33
b = 200

if b > a:
    print('b este mai mare')

# 2. if ... else
if a > b:
    print('a este mai mare')
else:
    print('b este mai mare')

# 3. if ... elif ... else
if a > b:
    print('a este mai mare')
elif b == a:
    print('sunt egale')
elif b == 0:
    print('b e 0')
else:
    print('b este mai tare')

# 4. if prescurtat
print('a') if a>b else print('b')
